// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract FundMeTrial {
    address public owner;
    address[] public funders;
    mapping(address => uint256) public fundersToFundMap;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }

    function getDatMonay() public payable {
        uint256 minimum = 5 * 10**18;
        require(msg.value < getConversionRate(minimum), "Not enough");
        fundersToFundMap[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getBalance() public view returns (uint256) {
        uint256 balance;
        for (uint256 i = 0; i < funders.length; i++) {
            balance += fundersToFundMap[funders[i]];
        }
        return balance;
    }

    function getConversionRate(uint256 _ether) public view returns (uint256) {
        uint256 etherPrice = getPrice();
        uint256 ethInUsd = (etherPrice * _ether) / 10000000000;
        return ethInUsd;
    }

    function getPrice() public view returns (uint256) {
        // AggregatorV3Interface priceFeed = AggregatorV3Interface(
        //     0x8A753747A1Fa494EC906cE90E9f37563A8AF630e
        // );
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        // ETH/USD rate in 18 digit
        return uint256(answer * 10000000000);
    }

    function getEntranceFee() public view returns (uint256) {
        uint256 minimumUSD = 50 * 10**10;
        uint256 price = getPrice();
        uint256 precission = 1 * 10**10;
        return (minimumUSD * precission) / price;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function withdraw() public payable onlyOwner {
        payable(msg.sender).transfer(address(this).balance);

        for (
            uint256 funderIndex = 0;
            funderIndex < funders.length;
            funderIndex++
        ) {
            address funder = funders[funderIndex];
            fundersToFundMap[funder] = 0;
        }
        funders = new address[](0);
    }
}
