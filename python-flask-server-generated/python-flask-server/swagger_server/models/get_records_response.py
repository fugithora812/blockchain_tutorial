# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util


class GetRecordsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """GetRecordsResponse - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'GetRecordsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetRecordsResponse of this GetRecordsResponse.  # noqa: E501
        :rtype: GetRecordsResponse
        """
        return util.deserialize_model(dikt, cls)
