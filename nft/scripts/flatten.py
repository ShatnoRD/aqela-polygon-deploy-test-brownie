#!/usr/bin/python3
from brownie import AdvancedCollectible, accounts, network, config, interface
import json


def main():
    flatten()


def flatten():
    with open("./AdvancedCollectible_flattened.json", "w") as file:
        json.dump(AdvancedCollectible.get_verification_info(), file)
