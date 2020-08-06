# coding: utf-8

"""
    Product Catalog APIs

    Ingram Micro product catalog API for requesting price and availability of SKUs in real time.  *Production URL - https://api.ingrammicro.com:443/resellers/v5*  # noqa: E501

    OpenAPI spec version: 5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.catalog_api import CatalogApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCatalogApi(unittest.TestCase):
    """CatalogApi unit test stubs"""

    def setUp(self):
        self.api = api.catalog_api.CatalogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_v5_catalog_productsearch(self):
        """Test case for get_v5_catalog_productsearch

        Search product catalog  # noqa: E501
        """
        pass

    def test_multi_sku_price_and_stock(self):
        """Test case for multi_sku_price_and_stock

        Find availability of upto 50 SKUs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()