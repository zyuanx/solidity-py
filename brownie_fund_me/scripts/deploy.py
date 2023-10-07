from brownie import FundMe, MockV3Aggregator, config, network
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)


def deploy_fund_me():
    account = get_account()
    gas_price(gas_strategy)
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
