// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LoanContract {
    address public owner;
    mapping(address => uint256) public balances;

    event LoanRequested(address indexed borrower, uint256 amount, bool approved);

    constructor() {
        owner = msg.sender;
    }

    function requestLoan(uint256 amount, bool approved) public {
        if (approved) {
            balances[msg.sender] += amount;
        }
        emit LoanRequested(msg.sender, amount, approved);
    }
}
