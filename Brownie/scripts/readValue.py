from brownie import SimpleStorage, accounts, config


def read_contract():
    print(SimpleStorage[0])
    # to work with the latest deployment we do -1
    # to work with the latest deployments we need their ABI and Address
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
