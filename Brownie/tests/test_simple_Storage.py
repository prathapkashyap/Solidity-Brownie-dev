from brownie import SimpleStorage, accounts


def test_deploy():
    # arrange
    account = accounts[0]
    # act
    simple_Storage = SimpleStorage.deploy({"from": account})

    starting_value = simple_Storage.retrieve()
    expected = 0
    # Asserting
    assert starting_value == expected

    pass


def test_update_storege():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    expected = 15
    simple_storage.store(expected, {"from": account})

    assert expected == simple_storage.retrieve()
