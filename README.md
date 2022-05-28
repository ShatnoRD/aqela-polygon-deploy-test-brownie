# Quickstart Guide

Shortened version of the official [Polygon](https://docs.polygon.technology/docs/develop/quicknode/) brownie guide

## Installation

In your current project Directory

```bash
pip3 install eth-brownie
```

## First steps

Load erc20,erc721 demo projects

```python
brownie bake token
brownie bake nft
```

Add custom network to brownie, using one of the free [RPC-s](https://docs.polygon.technology/docs/develop/network-details/network/#:~:text=https%3A//rpc%2Dmainnet.matic.quiknode.pro)

```python
brownie networks add Ethereum matic_mumbai host=https://rpc-mumbai.matic.today chainid=3
```

```output
SUCCESS: A new network 'matic_mumbai' has been added
  └─matic_mumbai
    ├─id: matic_mumbai
    ├─chainid: 3
    └─host: https://gasstation-mumbai.matic.today/v2
```

Generate a new demo wallet

```python
brownie accounts generate testac
```

```output
Generating a new private key...
mnemonic: 'attack state else draw mother mail adapt typical riot nothing object clump'
Enter the password to encrypt this account with:
aqela
SUCCESS: A new account '0x60552b1A4b53462681A2f123a95Aa8Efa686ec80' has been generated with the id 'testac'
```

Get some testnet MATIC from [Polygon Faucet](https://faucet.polygon.technology/) by submitting the address generated above.

## Deploying the contract

Change the directory to the desired demo project's root folder, then compile the contracts using

```python
brownie compile
```

```output
Compiling contracts...
  Solc version: 0.6.12
  Optimizer: Enabled  Runs: 200
  EVM Version: Istanbul
Generating build data...
 - SafeMath
 - Token

Project has been compiled. Build artifacts saved at C:\Users\antal\OneDrive\Dokumentumok\a q e l a\D E V\aqela-polygon-deploy-test-brownie\token\build\contracts
```

Go to scripts/token.py modify the code to use the wallet generated previously, instead of the default one

```python
#!/usr/bin/python3

from brownie import Token, accounts


def main():
    return Token.deploy("Test Token", "TST", 18, 1e21, {"from": accounts.load("testac")})

```

Deploy the contract by running the script we just modified to use the testnet MATIC

```python
brownie run token.py --network matic_mumbai
```

```output
TokenProject is the active project.

Running '\Users\antal\OneDrive\Dokumentumok\a q e l a\D E V\aqela-polygon-deploy-test-brownie\token\scripts\token.py::main'...
Enter password for "testac":
Transaction sent: 0x46b1079b33d3533a7e1b5e8b241223c9d5bb75fae0a261c7e05c4ff4861b76e9
  Gas price: 1.636248686 gwei   Gas limit: 573532   Nonce: 0
  Token.constructor confirmed   Block: 26503875   Gas used: 521393 (90.91%)
  Token deployed at: 0x9598538f51eA77F66cDa543F8B651b910da86447
```

Check out the deployed contract on [Polygonscan Mumbai](https://mumbai.polygonscan.com/address/0x9598538f51eA77F66cDa543F8B651b910da86447)
