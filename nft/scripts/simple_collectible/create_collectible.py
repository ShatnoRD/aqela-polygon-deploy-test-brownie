#!/usr/bin/python3
from brownie import SimpleCollectible, accounts, network, config
from scripts.helpful_scripts import OPENSEA_FORMAT

sample_token_uri = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def main():
    dev = accounts.from_mnemonic(config["wallets"]["from_mnemonic"])

    print(network.show_active())

    simple_collectible = SimpleCollectible[len(SimpleCollectible) - 1]

    token_id = simple_collectible.tokenCounter()
    transaction = simple_collectible.createCollectible(sample_token_uri, {"from": dev})

    transaction.wait(1)
    print(f"Awesome! You can view your NFT at {OPENSEA_FORMAT.format(simple_collectible.address, token_id)}")
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
