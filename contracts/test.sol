// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private storedNumber;

    // Function to store a number
    function setNumber(uint256 number) public {
        storedNumber = number;
    }

    // Function to retrieve the stored number
    function getNumber() public view returns (uint256) {
        return storedNumber;
    }
}
