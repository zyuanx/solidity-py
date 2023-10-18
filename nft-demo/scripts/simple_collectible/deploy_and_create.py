from brownie import SimpleCollectible, network
from scripts.helpful_scripts import OPENSEA_FORMAT, get_account

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awesome, you can view your NFT at {OPENSEA_FORMAT.format(simple_collectible.address, simple_collectible.tokenCounter()-1)}"
    )
    print("please wait up to 20 minutes")
    return simple_collectible


def main():
    deploy_and_create()
