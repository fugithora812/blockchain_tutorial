from web3 import Web3
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import json


class liquorDao:
    tokenId: int = 0
    userAccount: str = "0x594E436186fdd4415bf38EC89692521DA24Ed552"
    contractAddress: str = "0xD2476BC39B2F38c791b1a3D0E2F68Ad5988E71da"

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
        # DB接続
        engine = create_engine('sqlite:///app.db')

        # クエリ発行
        liquorId = -1
        with engine.connect() as con:
            rows = con.execute("select TOKEN_ID from liquor_table where LIQUOR_NAME='{}'".format(liquorName))
            for row in rows:
                liquorDict = dict(row)
                liquorId = int(liquorDict['TOKEN_ID'])

        return liquorId + 1

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

    def updateStockOnDB(liquorName: str) -> bool:
        # stockQuery = database.session.query(liquorModel)
        # stock_update = stockQuery.filter(
        #     liquorModel.LIQUOR_NAME == liquorName, liquorModel.SELLER_NAME == sellerName)

        # DB接続してクエリ発行
        engine = create_engine('sqlite:///app.db')
        stock_update = -1
        liquorId = -1
        with engine.connect() as con:
            rows = con.execute("select TOKEN_ID, STOCK_QUANTITY from liquor_table where LIQUOR_NAME='{}'".format(liquorName))
            for row in rows:
                liquorDict = dict(row)
                stock_update = int(liquorDict['STOCK_QUANTITY'])
                liquorId = int(liquorDict['TOKEN_ID'])

        print(stock_update)
        if stock_update - 1 < 0:
            liquorDao.updateReservabilityOnBC(liquorId)
            return False

        else:
            if stock_update - 1 == 0:
                liquorDao.updateReservabilityOnBC(liquorId)

            # ToDo: データベース更新処理実装
            newQuantity = stock_update - 1
            with engine.connect() as con:
                rows = con.execute(f"update liquor_table set STOCK_QUANTITY={newQuantity} where LIQUOR_NAME='{liquorName}' and TOKEN_ID={liquorId}")

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
        return liquors.functions.updateReservability(tokenId).transact({"from": liquorDao.userAccount})

    def addLiquor(liquorName: str, sellerName: str, isReservable: str, arrivalDay: str, stockQuantity: str):
        print(liquorName)
        print(sellerName)
        print(isReservable)
        print(arrivalDay)
        print(stockQuantity)

        web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
        pathToAbi = "dao/Liquor.json"

        json_open = open(pathToAbi, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        liquors = web3.eth.contract(address=liquorDao.contractAddress, abi=abi)
        json_open.close()
        liquors.functions.addBlockToRegister(
            liquorName, sellerName, isReservable, arrivalDay, stockQuantity).transact({"from": liquorDao.userAccount})

        engine = create_engine('sqlite:///app.db')

        # Todo: STOCK_QUANTITYのマジックナンバーは変える必要がある
        with engine.connect() as con:
            # DB接続してクエリ発行
            # con.execute("create table liquor_table( \
            #     LIQUOR_NAME STRING primary_key, \
            #     SELLER_NAME STRING primary_key, \
            #     STOCK_QUANTITY INTEGER, \
            #     TOKEN_ID INTEGER)")
            con.execute("insert into liquor_table values('{}', '{}', {}, {})".format(liquorName, sellerName, stockQuantity, liquorDao.tokenId))

        liquorDao.tokenId += 1
        return True
