from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    account = get_account()
    print("this account", account)
    # print(accou / nt)
    # from bronwie
    # account = accounts.load("localtest")
    # print(account)
    # Todo : check this method
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)d
    # Anytime we deploy to a chaing we need to metion the from account
    # print("simple storage", SimpleStorage.deploy())

    simple_storage = SimpleStorage.deploy({"from": account})
    print("simple storage", simple_storage)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_storage_value = simple_storage.retrieve()
    # print(updated_storage_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    print(" helloo")
    deploy_simple_storage()
