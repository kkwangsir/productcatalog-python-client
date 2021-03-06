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


class PriceAndAvailabilityRequestServicerequestPriceandstockrequest(object):
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
        'showwarehouseavailability': 'str',
        'extravailabilityflag': 'str',
        'includeallsystems': 'bool',
        'item': 'list[PriceAndAvailabilityRequestServicerequestPriceandstockrequestItem]'
    }

    attribute_map = {
        'showwarehouseavailability': 'showwarehouseavailability',
        'extravailabilityflag': 'extravailabilityflag',
        'includeallsystems': 'includeallsystems',
        'item': 'item'
    }

    def __init__(self, showwarehouseavailability=None, extravailabilityflag=None, includeallsystems=None, item=None):  # noqa: E501
        """PriceAndAvailabilityRequestServicerequestPriceandstockrequest - a model defined in Swagger"""  # noqa: E501
        self._showwarehouseavailability = None
        self._extravailabilityflag = None
        self._includeallsystems = None
        self._item = None
        self.discriminator = None
        if showwarehouseavailability is not None:
            self.showwarehouseavailability = showwarehouseavailability
        if extravailabilityflag is not None:
            self.extravailabilityflag = extravailabilityflag
        if includeallsystems is not None:
            self.includeallsystems = includeallsystems
        if item is not None:
            self.item = item

    @property
    def showwarehouseavailability(self):
        """Gets the showwarehouseavailability of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501

        True/false to show the availability of individual warehouses  # noqa: E501

        :return: The showwarehouseavailability of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501
        :rtype: str
        """
        return self._showwarehouseavailability

    @showwarehouseavailability.setter
    def showwarehouseavailability(self, showwarehouseavailability):
        """Sets the showwarehouseavailability of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.

        True/false to show the availability of individual warehouses  # noqa: E501

        :param showwarehouseavailability: The showwarehouseavailability of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501
        :type: str
        """

        self._showwarehouseavailability = showwarehouseavailability

    @property
    def extravailabilityflag(self):
        """Gets the extravailabilityflag of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501

        Y/N to show extra availability flag  # noqa: E501

        :return: The extravailabilityflag of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501
        :rtype: str
        """
        return self._extravailabilityflag

    @extravailabilityflag.setter
    def extravailabilityflag(self, extravailabilityflag):
        """Sets the extravailabilityflag of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.

        Y/N to show extra availability flag  # noqa: E501

        :param extravailabilityflag: The extravailabilityflag of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501
        :type: str
        """

        self._extravailabilityflag = extravailabilityflag

    @property
    def includeallsystems(self):
        """Gets the includeallsystems of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501

        Flag to indicate if the price and stock information is required for all Ingram Micro systems.  # noqa: E501

        :return: The includeallsystems of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501
        :rtype: bool
        """
        return self._includeallsystems

    @includeallsystems.setter
    def includeallsystems(self, includeallsystems):
        """Sets the includeallsystems of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.

        Flag to indicate if the price and stock information is required for all Ingram Micro systems.  # noqa: E501

        :param includeallsystems: The includeallsystems of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501
        :type: bool
        """

        self._includeallsystems = includeallsystems

    @property
    def item(self):
        """Gets the item of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501


        :return: The item of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501
        :rtype: list[PriceAndAvailabilityRequestServicerequestPriceandstockrequestItem]
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.


        :param item: The item of this PriceAndAvailabilityRequestServicerequestPriceandstockrequest.  # noqa: E501
        :type: list[PriceAndAvailabilityRequestServicerequestPriceandstockrequestItem]
        """

        self._item = item

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
        if issubclass(PriceAndAvailabilityRequestServicerequestPriceandstockrequest, dict):
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
        if not isinstance(other, PriceAndAvailabilityRequestServicerequestPriceandstockrequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
