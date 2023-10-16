import pytest
from brownie import accounts, exceptions, network
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS


def test_can_create_simple_collectible():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
