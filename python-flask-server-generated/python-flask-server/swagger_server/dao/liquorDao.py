from web3 import Web3
import sqlite3
import json


class liquorDao:
    tokenId: str

    def fetchDataFromDB(liquorName: str) -> int:
        return session.query(liquor_table.TOKEN_ID).filter(liquor_table.LIQUOR_NAME == liquorName)

    def fetchDataFromBC(tokenId: int) -> str:
        web3 = Web3(Web3.HttpProvider('http://localhost:7545'))
        pathToAbi = "../../BC_liquor/build/contracts"
        # hash = "0xf35b44d4b8b87b6730fd3e12ddcf41cd69c64e97c0cdeebb1b8d93199658f5fb"
        # print(web3.getTransactionReceipt(hash))

        json_open = open(path, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        contractAddress = "0xD12Ca9AaCBeFb6baD4de5A0D84FD324AD034bf40"
        liquors = web3.eth.contract(address=contractAddress, abi=abi)
        return liquors.methods.fetchLiquorData(tokenId).call()

    def updateStockOnDB(liquorName: str, sellerName: str) -> bool:
        stockQuery = session.query(liquor_table)
        stock_update = stockQuery.filter(
            liquor_table.LIQUOR_NAME == liquorName, liquor_table.SELLER_NAME == sellerName)
        stock_update.STOCK_QUANTITY -= 1

        if stock_update.STOCK_QUANTITY < 0:
            return False

        elif stock_update.STOCK_QUANTITY == 0:
            updateTokenId(stock_update.TOKEN_ID, stock_update)
            return True

        else:
            return True

        return False

    def changeBlock(tokenId: int) -> int:
        web3 = Web3(Web3.HttpProvider('http://localhost:7545'))
        pathToAbi = "../../BC_liquor/build/contracts"
        # hash = "0xf35b44d4b8b87b6730fd3e12ddcf41cd69c64e97c0cdeebb1b8d93199658f5fb"
        # print(web3.getTransactionReceipt(hash))

        json_open = open(path, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        contractAddress = "0xD12Ca9AaCBeFb6baD4de5A0D84FD324AD034bf40"
        liquors = web3.eth.contract(address=contractAddress, abi=abi)
        return liquors.methods.changeBlock(tokenId).call()

    def updateTokenId(tokenId: int, updateRow):
        newTokenId = changeBlock(tokenId)
        updateRow.TOKEN_ID = newTokenId
