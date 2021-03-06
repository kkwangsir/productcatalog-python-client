# coding: utf-8

"""
    Product Catalog APIs

    Ingram Micro product catalog API for requesting price and availability of SKUs in real time.  *Production URL - https://api.ingrammicro.com:443/resellers/v5*  # noqa: E501

    OpenAPI spec version: 5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class WarehouseListType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'warehouseid': 'str',
        'warehousedescription': 'str',
        'availablequantity': 'int',
        'onorderquantity': 'int',
        'onholdquantity': 'int',
        'etadate': 'str'
    }

    attribute_map = {
        'warehouseid': 'warehouseid',
        'warehousedescription': 'warehousedescription',
        'availablequantity': 'availablequantity',
        'onorderquantity': 'onorderquantity',
        'onholdquantity': 'onholdquantity',
        'etadate': 'etadate'
    }

    def __init__(self, warehouseid=None, warehousedescription=None, availablequantity=None, onorderquantity=None, onholdquantity=None, etadate=None):  # noqa: E501
        """WarehouseListType - a model defined in Swagger"""  # noqa: E501
        self._warehouseid = None
        self._warehousedescription = None
        self._availablequantity = None
        self._onorderquantity = None
        self._onholdquantity = None
        self._etadate = None
        self.discriminator = None
        if warehouseid is not None:
            self.warehouseid = warehouseid
        if warehousedescription is not None:
            self.warehousedescription = warehousedescription
        if availablequantity is not None:
            self.availablequantity = availablequantity
        if onorderquantity is not None:
            self.onorderquantity = onorderquantity
        if onholdquantity is not None:
            self.onholdquantity = onholdquantity
        if etadate is not None:
            self.etadate = etadate

    @property
    def warehouseid(self):
        """Gets the warehouseid of this WarehouseListType.  # noqa: E501


        :return: The warehouseid of this WarehouseListType.  # noqa: E501
        :rtype: str
        """
        return self._warehouseid

    @warehouseid.setter
    def warehouseid(self, warehouseid):
        """Sets the warehouseid of this WarehouseListType.


        :param warehouseid: The warehouseid of this WarehouseListType.  # noqa: E501
        :type: str
        """

        self._warehouseid = warehouseid

    @property
    def warehousedescription(self):
        """Gets the warehousedescription of this WarehouseListType.  # noqa: E501

        City of the Ingram Micro warehouse location  # noqa: E501

        :return: The warehousedescription of this WarehouseListType.  # noqa: E501
        :rtype: str
        """
        return self._warehousedescription

    @warehousedescription.setter
    def warehousedescription(self, warehousedescription):
        """Sets the warehousedescription of this WarehouseListType.

        City of the Ingram Micro warehouse location  # noqa: E501

        :param warehousedescription: The warehousedescription of this WarehouseListType.  # noqa: E501
        :type: str
        """

        self._warehousedescription = warehousedescription

    @property
    def availablequantity(self):
        """Gets the availablequantity of this WarehouseListType.  # noqa: E501

        On hand available quantity  # noqa: E501

        :return: The availablequantity of this WarehouseListType.  # noqa: E501
        :rtype: int
        """
        return self._availablequantity

    @availablequantity.setter
    def availablequantity(self, availablequantity):
        """Sets the availablequantity of this WarehouseListType.

        On hand available quantity  # noqa: E501

        :param availablequantity: The availablequantity of this WarehouseListType.  # noqa: E501
        :type: int
        """

        self._availablequantity = availablequantity

    @property
    def onorderquantity(self):
        """Gets the onorderquantity of this WarehouseListType.  # noqa: E501

        On Order quantity  # noqa: E501

        :return: The onorderquantity of this WarehouseListType.  # noqa: E501
        :rtype: int
        """
        return self._onorderquantity

    @onorderquantity.setter
    def onorderquantity(self, onorderquantity):
        """Sets the onorderquantity of this WarehouseListType.

        On Order quantity  # noqa: E501

        :param onorderquantity: The onorderquantity of this WarehouseListType.  # noqa: E501
        :type: int
        """

        self._onorderquantity = onorderquantity

    @property
    def onholdquantity(self):
        """Gets the onholdquantity of this WarehouseListType.  # noqa: E501

        On hold quantity  # noqa: E501

        :return: The onholdquantity of this WarehouseListType.  # noqa: E501
        :rtype: int
        """
        return self._onholdquantity

    @onholdquantity.setter
    def onholdquantity(self, onholdquantity):
        """Sets the onholdquantity of this WarehouseListType.

        On hold quantity  # noqa: E501

        :param onholdquantity: The onholdquantity of this WarehouseListType.  # noqa: E501
        :type: int
        """

        self._onholdquantity = onholdquantity

    @property
    def etadate(self):
        """Gets the etadate of this WarehouseListType.  # noqa: E501


        :return: The etadate of this WarehouseListType.  # noqa: E501
        :rtype: str
        """
        return self._etadate

    @etadate.setter
    def etadate(self, etadate):
        """Sets the etadate of this WarehouseListType.


        :param etadate: The etadate of this WarehouseListType.  # noqa: E501
        :type: str
        """

        self._etadate = etadate

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WarehouseListType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WarehouseListType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
