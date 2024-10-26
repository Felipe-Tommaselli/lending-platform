from web3 import Web3
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from classifier import predict_risk

# Connect to Ganache
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if web3.is_connected():
    print("Connected to Ganache")
else:
    print("Failed to connect to Ganache")

# Define the contract address and ABI
contract_address = "0xc4427930D51B5f5e540CF4D5cA7E4A7D2D5E5F99"  # Replace with your deployed contract address
contract_abi = [
    {
        "constant": False,
        "inputs": [{"name": "amount", "type": "uint256"}, {"name": "approved", "type": "bool"}],
        "name": "requestLoan",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getLoanBalance",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
]

# Access the contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Select an unlocked account from Ganache
account = web3.eth.accounts[0]  # Using the first Ganache account

# Function to request a loan with AI decision
def request_loan(amount, credit_score, debt):
    balance = contract.functions.getLoanBalance().call({'from': account})
    approved = predict_risk(credit_score, balance, debt)
    txn_hash = contract.functions.requestLoan(amount, approved).transact({'from': account})
    web3.eth.wait_for_transaction_receipt(txn_hash)
    print(f"Loan request for {amount} submitted. Approved: {approved}")

# Function to check loan balance
def get_loan_balance():
    balance = contract.functions.getLoanBalance().call({'from': account})
    print(f"Loan balance for account {account}: {balance}")

if __name__ == "__main__":
    while True:
        print("1. Request Loan")
        print("2. Check Loan Balance")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            amount = int(input("Enter loan amount: "))
            score = input("Enter credit score and debt: ").split(','.strip())
            credit_score = int(score[0])
            debt = int(score[1])
            request_loan(amount, credit_score, debt)
        elif choice == "2":
            get_loan_balance()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")