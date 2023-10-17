from scripts.deploy_and_create import deploy_and_create
import pytest
from brownie import accounts, exceptions, network
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account


def test_can_create_simple_collectible():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_account()
