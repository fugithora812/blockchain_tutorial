import json
import connexion
import six

from models.get_records_response import GetRecordsResponse  # noqa: E501
from models.post_records_request import PostRecordsRequest  # noqa: E501
import util

import dao.liquorDao

# APIへのgetリクエスト時の処理


def records_get():  # noqa: E501
    """酒類在庫取得API"""
    # 本番では消す必要がある
    liquorDao.addLiquor("sake", "ore", true, "2020/12/16", "1")

    allData = liquorDao.getAllDataFromBC()
    return json.dumps(allData)


def liquors_reserve(path):  # noqa: E501
    """酒類取り置き依頼の処理API"""
    return liquorDao.updateStockOnDB(liquorName, sellerName)


def liquors_search(liquorName):
    """酒類在庫検索API"""
    tokenId = liquorDao.fetchDataFromDB(searchWord)
    liquorData = liquorDao.fetchDataFromBC(tokenId)
    return json.dumps(liquorData)
