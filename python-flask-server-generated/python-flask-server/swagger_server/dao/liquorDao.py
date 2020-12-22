from web3 import Web3
# from flask_sqlalchemy import SQLAlchemy
from dao import database, liquorModel
import json


class liquorDao:
    tokenId: int = 0
    userAccount: str = "0x53D68C2FD18Dca23fC9b904f52D5C65f5694b32e"
    contractAddress: str = "0x1534193aeF6cbeb1c240c441Af10A8d05e6E3BDe"

    def fetchLiquorFromBC(tokenId: int) -> str:
        web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
        pathToAbi = "dao/Liquor.json"

        json_open = open(pathToAbi, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        liquors = web3.eth.contract(address=liquorDao.contractAddress, abi=abi)
        json_open.close()
        return liquors.functions.fetchLiquor(tokenId).transact()

    def fetchTokenIdFromDB(liquorName: str) -> int:
        return database.session.query(liquorModel.liquor_table.TOKEN_ID).filter(liquorModel.LIQUOR_NAME == liquorName)

    def fetchAllLiquorsFromBC():
        web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
        pathToAbi = "dao/Liquor.json"

        json_open = open(pathToAbi, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        liquors = web3.eth.contract(address=liquorDao.contractAddress, abi=abi)
        json_open.close()

        # these are from https://web3py.readthedocs.io/en/latest/overview.html#contracts
        # tx_hash = liquors.constructor().transact()
        # tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        # tx_receipt.contractAddress
        # deployed_contract = web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
        # return deployed_contract.functions.fetchAllLiquors().call()

        # return json.dump(liquors.functions.fetchAllLiquors().transact())
        return liquors.functions.fetchAllLiquors().call()

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
        liquors = web3.eth.contract(address=liquorDao.contractAddress, abi=abi)
        json_open.close()
        return liquors.functions.updateReservability(tokenId).transact()

    def addLiquor(liquorName: str, sellerName: str, isReservable: str, arrivalDay: str, reserveScore: str):
        print(liquorName)
        print(sellerName)
        print(isReservable)
        print(arrivalDay)
        print(reserveScore)

        web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
        pathToAbi = "dao/Liquor.json"

        json_open = open(pathToAbi, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        liquors = web3.eth.contract(address=liquorDao.contractAddress, abi=abi)
        json_open.close()
        liquors.functions.addBlockToRegister(
            liquorName, sellerName, isReservable, arrivalDay, reserveScore).transact({"from": liquorDao.userAccount})

        # Todo: STOCK_QUANTITYのマジックナンバーは変える必要がある
        liquorDao.tokenId += 1
        newLiquor = liquorModel.Liquor()
        newLiquor.LIQUOR_NAME = liquorName
        newLiquor.SELLER_NAME = sellerName
        newLiquor.STOCK_QUANTITY = 1
        newLiquor.TOKEN_ID = liquorDao.tokenId

        return True
