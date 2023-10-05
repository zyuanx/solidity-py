from solcx import compile_standard, install_solc


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

print(compiled_sol)
