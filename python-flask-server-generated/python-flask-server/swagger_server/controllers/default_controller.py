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

    return dao.liquorDao.liquorDao.fetchAllLiquorsFromBC()


def liquors_add(liquorName, sellerName, isReservable, arrivalDay, reserveScore):
    return dao.liquorDao.liquorDao.addLiquor(liquorName, sellerName, isReservable, arrivalDay, reserveScore)
    # return True


def liquors_reserve(liquorName, sellerName):  # noqa: E501
    """酒類取り置き依頼の処理API"""
    return dao.liquorDao.liquorDao.updateStockOnDB(liquorName, sellerName)


def liquors_search(liquorName):
    """酒類在庫検索API"""
    tokenId = dao.liquorDao.liquorDao.fetchTokenIdFromDB(liquorName)
    liquorData = dao.liquorDao.liquorDao.fetchLiquorFromBC(tokenId)
    # return json.dumps(liquorData)
    return liquorData
