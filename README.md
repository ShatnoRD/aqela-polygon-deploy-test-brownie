# Quickstart Guide

Shortened version of the official [Polygon](https://docs.polygon.technology/docs/develop/quicknode/) development using brownie guide

## Installation

In your current project Directory

```bash
pip3 install eth-brownie
```

## First steps

Load erc20, erc721 demo projects

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

## Deploying ERC20

Change the directory to the desired ERC20 demo project's root folder, then compile the contracts using

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

Project has been compiled. Build artifacts saved
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

Enter password for "testac":
aqela
Transaction sent: 0x46b1079b33d3533a7e1b5e8b241223c9d5bb75fae0a261c7e05c4ff4861b76e9
  Gas price: 1.636248686 gwei   Gas limit: 573532   Nonce: 0
  Token.constructor confirmed   Block: 26503875   Gas used: 521393 (90.91%)
  Token deployed at: 0x9598538f51eA77F66cDa543F8B651b910da86447
```

Check out the deployed [contract](https://mumbai.polygonscan.com/address/0x9598538f51eA77F66cDa543F8B651b910da86447)

## Deploying ERC721

Change the directory to the ERC721 demo project's root folder, then compile the contracts using

```python
brownie compile
```

```output
Brownie v1.17.1 - Python development framework for Ethereum

865kiB [00:00, 2.75MiB/s]
WARNING: Unable to compile smartcontractkit/chainlink-brownie-contracts@1.1.1 due to a UnicodeDecodeError - you may still be able to import sources from the package, but will be unable to load the package directly.

Downloading from https://solc-bin.ethereum.org/windows-amd64/solc-windows-amd64-v0.4.26+commit.4563c3fc.zip
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5.76M/5.76M [00:02<00:00, 2.35MiB/s]
solc 0.4.26 successfully installed
Downloading from https://solc-bin.ethereum.org/windows-amd64/solc-windows-amd64-v0.6.6+commit.6c089d02.zip
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7.20M/7.20M [00:03<00:00, 1.92MiB/s]
solc 0.6.6 successfully installed
Compiling contracts...
  Solc version: 0.6.6
  Optimizer: Enabled  Runs: 200
  EVM Version: Istanbul
Generating build data...
 - OpenZeppelin/openzeppelin-contracts@3.4.0/ERC165
 - OpenZeppelin/openzeppelin-contracts@3.4.0/IERC165
 - OpenZeppelin/openzeppelin-contracts@3.4.0/SafeMath
 - OpenZeppelin/openzeppelin-contracts@3.4.0/ERC721
 - OpenZeppelin/openzeppelin-contracts@3.4.0/IERC721
 - OpenZeppelin/openzeppelin-contracts@3.4.0/IERC721Enumerable
 - OpenZeppelin/openzeppelin-contracts@3.4.0/IERC721Metadata
 - OpenZeppelin/openzeppelin-contracts@3.4.0/IERC721Receiver
 - OpenZeppelin/openzeppelin-contracts@3.4.0/Address
 - smartcontractkit/chainlink-brownie-contracts@1.1.1/ERC677Token
 - smartcontractkit/chainlink-brownie-contracts@1.1.1/ERC20
 - smartcontractkit/chainlink-brownie-contracts@1.1.1/ERC20Basic
 - smartcontractkit/chainlink-brownie-contracts@1.1.1/ERC677
 - smartcontractkit/chainlink-brownie-contracts@1.1.1/ERC677Receiver
 - smartcontractkit/chainlink-brownie-contracts@1.1.1/BasicToken
 - smartcontractkit/chainlink-brownie-contracts@1.1.1/SafeMathChainlink
 - smartcontractkit/chainlink-brownie-contracts@1.1.1/StandardToken
 - LinkToken

Compiling contracts...
  Solc version: 0.8.9
  Optimizer: Enabled  Runs: 200
  EVM Version: Istanbul
Generating build data...
 - Base64

Generating interface ABIs...
Project has been compiled. Build artifacts saved
```

Add mnemonic of previously generated wallet to .env
change the accounts.add to accounts.from_mnemonic to use from_mnemonic in scripts/simple_collectible/create_collectible.py and scripts/simple_collectible/deploy_simple.py

```python
#!/usr/bin/python3
dev = accounts.from_mnemonic(config["wallets"]["from_mnemonic"])
```

Deploy the contract

```python
brownie run scripts\simple_collectible\deploy_simple.py --network matic_mumbai
```

```output
matic_mumbai
Transaction sent: 0xf638c26dbb5d34404e0f3558990b7b3adbdf4542651c253555a35c7668a4256b
  Gas price: 1.500000011 gwei   Gas limit: 2017282   Nonce: 1
  SimpleCollectible.constructor confirmed   Block: 26514226   Gas used: 1833893 (90.91%)
  SimpleCollectible deployed at: 0xF93adb21326300B231a2b2e1864BD86b2668432b
```

Check out the deployed [contract](https://mumbai.polygonscan.com/address/0xF93adb21326300B231a2b2e1864BD86b2668432b)

Mint an NFT on the deployed contract using the example scripts

```python
brownie run scripts\simple_collectible\create_collectible.py --network matic_mumbai
```

```output
matic_mumbai
Transaction sent: 0xcaa596a2414bc521e129f4e753b25f9cad8932b85518428c6f44ae02c306a9e0
  Gas price: 1.701063129 gwei   Gas limit: 279109   Nonce: 2
  SimpleCollectible.createCollectible confirmed   Block: 26514257   Gas used: 253736 (90.91%)

  SimpleCollectible.createCollectible confirmed   Block: 26514257   Gas used: 253736 (90.91%)

Awesome! You can view your NFT at https://testnets.opensea.io/assets/0xF93adb21326300B231a2b2e1864BD86b2668432b/0
Please give up to 20 minutes, and hit the "refresh metadata" button
```

The since the sample_token_uri is set to a no longer accessible uri source, the deployed token's uri will return 404 not found as well, but the minting was succesfull as you can see the [transaction](https://mumbai.polygonscan.com/tx/0xcaa596a2414bc521e129f4e753b25f9cad8932b85518428c6f44ae02c306a9e0) containing the createCollectible function call
