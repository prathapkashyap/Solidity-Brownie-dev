// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    //  uint  = unsigned integer
    uint256 myNumber = 455;
    bool myBool = true;
    string myName = "not my name";
    int256 signedNumber = -568;
    address ethAddress = 0x8C6a0698f3c4616cA2B1A0Bd3D2DF36ee84854c9;
    bytes32 myBytes = "cat";

    //A uint will always be initialized to 0 although its not given a value
    uint256 public favouriteNumber;
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People public person = People({favoriteNumber: 2, name: "pnk"});

    People[] public people;
    mapping(string => uint256) public nameToFavNo;

    function store(uint256 _favoriteNumber) public returns (uint256) {
        favouriteNumber = _favoriteNumber;
        return _favoriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favouriteNumber;
    }

    function add(uint256 adder) public pure {
        adder + adder;
    }

    function addPerson(string memory _name, uint256 _favNumber) public {
        people.push(People({favoriteNumber: _favNumber, name: _name}));
        nameToFavNo[_name] = _favNumber;
    }
}
