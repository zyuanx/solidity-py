from scripts.helpful_scripts import get_account, fund_with_link
from brownie import AdvancedCollectible, network, config


def main():
    account = get_account
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("Collectible created!")
