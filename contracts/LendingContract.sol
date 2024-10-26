// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LendingPlatform {
    address public owner;

    // Mapping to track user loan balances
    mapping(address => uint256) public loanBalances;

    // Event to log loan requests
    event LoanRequested(address indexed borrower, uint256 amount, bool approved);

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to request a loan
    function requestLoan(uint256 amount, bool approved) public {
        if (approved) {
            loanBalances[msg.sender] += amount;
        }

        // Emit the loan request event
        emit LoanRequested(msg.sender, amount, approved);
    }

    // Function to check the loan balance of a user
    function getLoanBalance() public view returns (uint256) {
        return loanBalances[msg.sender];
    }
}
