from web3 import Web3
from sqlalchemy import create_engine
import json


class liquorDao:
    tokenId: int = 0
    userAccount: str = "0x8D78e14Dedaf4b75C7F6C3c0E5a54241a8A6D044"
    contractAddress: str = "0x81A6FbE8C6977C4c640dF28f6310f3aAAc3D040b"

    # 指定したIDの商品１点を表示
    def fetchLiquorFromBC(searchId: int) -> str:
        web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
        pathToAbi = "dao/Liquor.json"

        json_open = open(pathToAbi, "r")
        json_load = json.load(json_open)

        abi = json_load["abi"]
        liquors = web3.eth.contract(address=liquorDao.contractAddress, abi=abi)
        json_open.close()
        liquorContent = liquors.functions.fetchLiquor(searchId - 1).call()
        contentName = ["liquorName", "sellerName", "isReservable", "arrivalDay", "stockQuantity"]
        contentList = []
        contentList.append(dict(zip(contentName, liquorContent)))

        return contentList

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

        # 要素数を数え、順にリストに追加
        contents = liquors.functions.fetchAllLiquors().call()
        liquorNum = len(contents)

        contentName = ["liquorName", "sellerName", "isReservable", "arrivalDay", "stockQuantity"]
        contentList = []
        for number in range(int(liquorNum / 5)):
            tmpList = [contents[(5 * number)], contents[(5 * number) + 1],
                       contents[(5 * number) + 2], contents[(5 * number) + 3], contents[(5 * number) + 4]]
            contentList.append(dict(zip(contentName, tmpList)))

        return contentList

    def updateStockOnDB(liquorName: str) -> bool:
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

        if stock_update - 1 < 0:
            liquorDao.updateReservabilityOnBC(liquorId)
            return False

        else:
            if stock_update - 1 == 0:
                liquorDao.updateReservabilityOnBC(liquorId)

            # ? DBの在庫数更新(あくまでも「予約」機能なので必要なし？)
            # newQuantity = stock_update - 1
            # with engine.connect() as con:
            #     con.execute("update liquor_table set STOCK_QUANTITY={} where LIQUOR_NAME='{}' and TOKEN_ID={}".format(newQuantity, liquorName, liquorId))

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
