from brownie import FundMeTrial, network, config
from scripts.helpful_scripts import get_account, get_pricefeed_address
import os


def deploy_fund_me():
    account = get_account()
    # print(
    #     os.environ["ETHERSCAN_TOKEN"],
    #     config["networks"],
    # )
    print(network.show_active())
    fund_me = FundMeTrial.deploy(
        get_pricefeed_address(),
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )

    # fund_me.fund(6)
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
