# import json
# import connexion
# import six

# from models.get_records_response import GetRecordsResponse  # noqa: E501
# from models.post_records_request import PostRecordsRequest  # noqa: E501
# import util

import dao.liquorDao

# APIへのgetリクエスト時の処理


def liquors_get():  # noqa: E501
    """酒類在庫取得API"""

    # 以下の2行は本番では消す必要がある
    dao.liquorDao.liquorDao.addLiquor("sake", "ore", True, "2020/12/16", "1")
    print("hello")

    allData = dao.liquorDao.liquorDao.fetchAllLiquorsFromBC()
    # return json.dumps(allData)
    return allData


def liquors_reserve(liquorName, sellerName):  # noqa: E501
    """酒類取り置き依頼の処理API"""
    return dao.liquorDao.liquorDao.updateStockOnDB(liquorName, sellerName)


def liquors_search(liquorName):
    """酒類在庫検索API"""
    tokenId = dao.liquorDao.liquorDao.fetchTokenIdFromDB(liquorName)
    liquorData = dao.liquorDao.liquorDao.fetchLiuorFromBC(tokenId)
    # return json.dumps(liquorData)
    return liquorData
