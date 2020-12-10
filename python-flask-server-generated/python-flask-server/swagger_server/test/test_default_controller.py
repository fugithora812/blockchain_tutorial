# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_records_response import GetRecordsResponse  # noqa: E501
from swagger_server.models.post_records_request import PostRecordsRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_records_get(self):
        """Test case for records_get

        酒類在庫取得API
        """
        response = self.client.open(
            '/api/v1/records',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_records_post(self):
        """Test case for records_post

        酒類在庫検索API
        """
        body = PostRecordsRequest()
        response = self.client.open(
            '/api/v1/records',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
