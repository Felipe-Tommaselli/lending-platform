from web3 import Web3

# Connect to Ganache
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if web3.is_connected():
    print("Connected to Ganache")
else:
    print("Failed to connect to Ganache")

# Define the contract address and ABI
contract_address = "0x5b7779726cAdb589E5D027F4424cE513bF2FB96e"  # Replace with your deployed contract address
contract_abi = [
    {
        "constant": False,
        "inputs": [{"name": "number", "type": "uint256"}],
        "name": "setNumber",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getNumber",
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

# Function to set a number in the contract
def set_number(value):
    # Send transaction without signing manually
    txn_hash = contract.functions.setNumber(value).transact({'from': account})
    web3.eth.wait_for_transaction_receipt(txn_hash)
    print(f"Stored {value} in contract")

# Function to get the number from the contract
def get_number():
    value = contract.functions.getNumber().call()
    print(f"Retrieved value from contract: {value}")

# Test the functions
set_number(42)
get_number()
