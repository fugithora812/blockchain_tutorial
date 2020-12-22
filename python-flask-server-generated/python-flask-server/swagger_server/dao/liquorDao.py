from web3 import Web3
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dao import database, liquorModel
import json


class liquorDao:
    tokenId: int = 0
    userAccount: str = "0x53D68C2FD18Dca23fC9b904f52D5C65f5694b32e"
    contractAddress: str = "0xAd835682B7063e88F108bfCB0DcE4f5160D839CF"

    def fetchLiquorFromBC(searchId: int) -> str:
        web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
        pathToAbi = "dao/Liquor.json"

        json_open = open(pathToAbi, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        liquors = web3.eth.contract(address=liquorDao.contractAddress, abi=abi)
        json_open.close()
        return liquors.functions.fetchLiquor(searchId - 1).call()

    def fetchTokenIdFromDB(liquorName: str) -> int:
        engine = create_engine('sqlite:///app.db')

        liquorId = -1
        # liquorIdstr = ""
        with engine.connect() as con:
            rows = con.execute("select TOKEN_ID from liquor_table where LIQUOR_NAME='{}'".format(liquorName))
            for row in rows:
                liquorDict = dict(row)
                liquorId = int(liquorDict['TOKEN_ID'])

        # print(type(liquorIdstr))
        # print(liquorIdstr)
        # liquorId = int(liquorIdstr)

        # return database.session.query(liquorModel.Liquor.liquor_table.TOKEN_ID).filter(liquorModel.LIQUOR_NAME == liquorName)

        return liquorId

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

        liquorNum = len(liquors.functions.fetchAllLiquors().call())
        numList = []
        for number in range(liquorNum):
            numList.append(number)

        # listLiquor = liquors.functions.fetchAllLiquors().call()
        # liquorNames = []
        # for liq in listLiquor:
        #     liquorName = ""
        #     for letter in liq:
        #         print(ord(letter))
        #         liquorName += ord(letter)
        #     liquorNames.append(liquorName)

        # liquorDict = dict(zip(numList, listLiquor))
        # return json.dumps(liquorDict)
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

        engine = create_engine('sqlite:///app.db')

        # Todo: STOCK_QUANTITYのマジックナンバーは変える必要がある
        with engine.connect() as con:
            # con.execute("create table liquor_table( \
            #     LIQUOR_NAME STRING primary_key, \
            #     SELLER_NAME STRING primary_key, \
            #     STOCK_QUANTITY INTEGER, \
            #     TOKEN_ID INTEGER)")
            con.execute("insert into liquor_table values('{}', '{}', {}, {})".format(liquorName, sellerName, 1, liquorDao.tokenId))

        liquorDao.tokenId += 1
        return True
