from web3 import Web3
import sqlite3
import json


class liquorDao:
    tokenId: int = 0
    liquors = ""

    def getConnectionWithBC():
        web3 = Web3(Web3.HttpProvider('http://localhost:7545'))
        pathToAbi = "../../BC_liquor/build/contracts"

        json_open = open(pathToAbi, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        contractAddress = "0xD12Ca9AaCBeFb6baD4de5A0D84FD324AD034bf40"
        liquors = web3.eth.contract(address=contractAddress, abi=abi)
        json_open.close()

    def fetchLiquorFromBC(tokenId: int) -> str:
        getConnectionWithBC()
        return liquors.methods.fetchLiquorData(tokenId).call()

    def fetchTokenIdFromDB(liquorName: str) -> int:
        return session.query(liquor_table.TOKEN_ID).filter(liquor_table.LIQUOR_NAME == liquorName)

    def fetchAllLiquorsFromBC() -> str[]:
        getConnectionWithBC()
        return liquors.methods.fetchAllLiquors().call()

    def updateStockOnDB(liquorName: str, sellerName: str) -> bool:
        stockQuery = session.query(liquor_table)
        stock_update = stockQuery.filter(
            liquor_table.LIQUOR_NAME == liquorName, liquor_table.SELLER_NAME == sellerName)

        if stock_update.STOCK_QUANTITY - 1 < 0:
            updateReservabilityOnBC(stock_update.TOKEN_ID)
            return False

        elif stock_update.STOCK_QUANTITY - 1 == 0:
            updateReservabilityOnBC(stock_update.TOKEN_ID)
            return True

        else:
            return True

        return False

    def updateReservabilityOnBC(tokenId: int) -> int:
        getConnectionWithBC()
        return liquors.methods.updateReservability(tokenId).call()
