import json
import connexion
import six

from swagger_server.models.get_records_response import GetRecordsResponse  # noqa: E501
from swagger_server.models.post_records_request import PostRecordsRequest  # noqa: E501
from swagger_server import util

import.. / liquorDao

# APIへのgetリクエスト時の処理


def records_get():  # noqa: E501
    """酒類在庫取得API"""

    allData = liquorDao.getAllDataFromBC()
    return json.dumps(allData)


def records_post(body):  # noqa: E501
    """酒類取り置き依頼の処理API"""
    return liquorDao.updateStockOnDB(liquorName, sellerName)


def records_put(searchWord):
    """酒類在庫検索API"""
    tokenId = liquorDao.fetchDataFromDB(searchWord)
    liquorData = liquorDao.fetchDataFromBC(tokenId)
    return json.dumps(liquorData)
