from web3 import Web3
import sqlite3
import json


class liquorDao:
    tokenId: string

    def fetchDataFromBC(tokenId: int) -> string:
        web3: Web3 = new Web3(web3.currentProvider)
        pathToAbi = "../../BC_liquor/build/contracts"
        # hash = "0xf35b44d4b8b87b6730fd3e12ddcf41cd69c64e97c0cdeebb1b8d93199658f5fb"
        # print(web3.getTransactionReceipt(hash))

        json_open = open(path, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        contractAddress = "0xD12Ca9AaCBeFb6baD4de5A0D84FD324AD034bf40"
        liquors = web3.eth.contract(address=contractAddress, abi=abi)
        return liquors.methods.fetchLiquorData(tokenId).call()
