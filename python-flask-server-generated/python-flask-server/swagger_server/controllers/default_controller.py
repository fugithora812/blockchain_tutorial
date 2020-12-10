import connexion
import six

from swagger_server.models.get_records_response import GetRecordsResponse  # noqa: E501
from swagger_server.models.post_records_request import PostRecordsRequest  # noqa: E501
from swagger_server import util

# APIへのgetリクエスト時の処理


def records_get():  # noqa: E501
    """酒類在庫取得API

    # noqa: E501


    :rtype: GetRecordsResponse
    """
    return 'do some magic!'


def records_post(body):  # noqa: E501
    """酒類取り置き依頼の処理API

    # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostRecordsRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def records_put(searchWord):
    """酒類在庫検索API

    """
    return "do some magic!"
