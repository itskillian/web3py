from web3 import Web3, EthereumTesterProvider

w3 = Web3(EthereumTesterProvider())

w3.is_connected()

latest_block = w3.eth.get_block('latest')

with open('block.txt', 'w') as file:
    for key, value in latest_block.items():
        output = str(key) + ': ' + str(value) + '\n'
        file.write(output)

w3.is_address()