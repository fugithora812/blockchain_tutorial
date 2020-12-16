from web3 import Web3
# from flask_sqlalchemy import SQLAlchemy
from dao import database, liquorModel
import json


class liquorDao:
    tokenId: int = 0
    userAccount = "0x8090796d9a4d93BdccAEABB86c40cEfF8F51de0b"

    def fetchLiquorFromBC(tokenId: int) -> str:
        web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
        pathToAbi = "dao/Liquor.json"

        json_open = open(pathToAbi, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        contractAddress = "0x1e2489ebded5b3156817d5280b0ed700abbfe375"
        liquors = web3.eth.contract(address=contractAddress, abi=abi)
        json_open.close()
        return liquors.functions.fetchLiquor(tokenId).transact()

    def fetchTokenIdFromDB(liquorName: str) -> int:
        return database.session.query(liquorModel.liquor_table.TOKEN_ID).filter(liquorModel.LIQUOR_NAME == liquorName)

    def fetchAllLiquorsFromBC() -> str:
        web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
        pathToAbi = "dao/Liquor.json"

        json_open = open(pathToAbi, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        contractAddress = "0x1e2489ebded5b3156817d5280b0ed700abbfe375"
        liquors = web3.eth.contract(address=contractAddress, abi=abi)
        json_open.close()
        return liquors.functions.fetchAllLiquors().transact()

    def updateStockOnDB(liquorName: str, sellerName: str) -> bool:
        stockQuery = database.session.query(liquorModel)
        stock_update = stockQuery.filter(
            liquorModel.LIQUOR_NAME == liquorName, liquorModel.SELLER_NAME == sellerName)

        if stock_update.STOCK_QUANTITY - 1 < 0:
            liquorDao.updateReservabilityOnBC(stock_update.TOKEN_ID)
            return False

        elif stock_update.STOCK_QUANTITY - 1 == 0:
            liquorDao.updateReservabilityOnBC(stock_update.TOKEN_ID)
            return True

        else:
            return True

        return False

    def updateReservabilityOnBC(tokenId: int) -> int:
        web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
        pathToAbi = "dao/Liquor.json"

        json_open = open(pathToAbi, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        contractAddress = "0x1e2489ebded5b3156817d5280b0ed700abbfe375"
        liquors = web3.eth.contract(address=contractAddress, abi=abi)
        json_open.close()
        return liquors.functions.updateReservability(tokenId).transact()

    def addLiquor(liquorName: str, sellerName: str, isReservable: bool, arrivalDay: str, reserveScore: str):
        web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
        pathToAbi = "dao/Liquor.json"

        json_open = open(pathToAbi, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        contractAddress = "0x1e2489ebded5b3156817d5280b0ed700abbfe375"
        liquors = web3.eth.contract(address=contractAddress, abi=abi)
        json_open.close()
        liquors.functions.addBlockToRegister(
            liquorName, sellerName, isReservable, arrivalDay, reserveScore).transact()

        # STOCK_QUANTITYのマジックナンバーは変える必要がある
        liquorDao.tokenId += 1
        newLiquor = liquorModel.Liquor()
        newLiquor.LIQUOR_NAME = liquorName
        newLiquor.SELLER_NAME = sellerName
        newLiquor.STOCK_QUANTITY = 1
        newLiquor.TOKEN_ID = liquorDao.tokenId
