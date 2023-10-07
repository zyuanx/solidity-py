# Brownie Fund Me

```
      - chainid: 11155111
        explorer: https://api-sepolia.etherscan.io/api
        host: https://sepolia.infura.io/v3/$WEB3_INFURA_PROJECT_ID
        id: sepolia
        name: Sepolia (Infura)
        provider: infura
```

add this to ~/.brownie/network-config.yaml

```
brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.g.alchemy.com/v2/xxxxx port=8545 accounts=10 mnemonic=brownie
```
