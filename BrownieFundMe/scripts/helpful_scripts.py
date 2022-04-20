from distutils.command.config import config
from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

FORKED__LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-development"]
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]

DECIMALS = 18
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT
        or network.show_active() in FORKED__LOCAL_ENVIRONMENT
    ):
        print("in development env")
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_pricefeed_address():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        print("config", config["networks"])
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed_address"
        ]
        print("price feed address", price_feed_address)
        return price_feed_address
    else:
        print("in mocking part", MockV3Aggregator)
        if len(MockV3Aggregator) <= 0:

            print(f"the active network is {network.show_active()}")
            # print("deploying mocks.....")
            MockV3Aggregator.deploy(
                DECIMALS, Web3.toWei(2000, "ether"), {"from": get_account()}
            )
            # print(f"mock deployed at {mock_v3_aggregator.address}")
        return MockV3Aggregator[-1].address
