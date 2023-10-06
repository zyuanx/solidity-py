import json
import os
from dotenv import load_dotenv
from solcx import compile_standard, install_solc
from web3 import Web3


load_dotenv()
with open('./SimpleStorage.sol', 'r', encoding='utf-8') as f:
    simple_storage_file = f.read()

install_solc("0.6.0")
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
            }
        }
    }
}, solc_version="0.6.0")

with open('compiled_code.json', 'w', encoding='utf-8') as f:
    json.dump(compiled_sol, f)


bytecode = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']

abi = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']


# For connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
CHAIN_ID = 1337
MY_ADDRESS = '0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1'
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)
nonce = w3.eth.get_transaction_count(MY_ADDRESS)
transaction = SimpleStorage.constructor().build_transaction({
    'chainId': CHAIN_ID,
    'from': MY_ADDRESS,
    'nonce': nonce,
})
signed_txn = w3.eth.account.sign_transaction(
    transaction, private_key=PRIVATE_KEY
)
print("Deploying contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed!")

# Working with the contract
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(simple_storage.functions.retrieve().call())
store_transaction = simple_storage.functions.store(15).build_transaction({
    'chainId': CHAIN_ID,
    'from': MY_ADDRESS,
    'nonce': nonce + 1,
})
signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=PRIVATE_KEY
)

send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
print(simple_storage.functions.retrieve().call())
