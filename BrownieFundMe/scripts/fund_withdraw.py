from brownie import FundMeTrial
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMeTrial[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print("entree fee", entrance_fee)
    fund_me.getDatMonay({"from": account, "value": entrance_fee})
    print("balance", fund_me.getBalance())


def withdraw():
    fund_me = FundMeTrial[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
