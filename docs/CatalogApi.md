# swagger_client.CatalogApi

All URIs are relative to *https://api.ingrammicro.com:443/sandbox/resellers/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v5_catalog_productsearch**](CatalogApi.md#get_v5_catalog_productsearch) | **GET** /catalog | Search product catalog
[**multi_sku_price_and_stock**](CatalogApi.md#multi_sku_price_and_stock) | **POST** /catalog/priceandavailability | Find availability of upto 50 SKUs

# **get_v5_catalog_productsearch**
> ProductSearchResponse get_v5_catalog_productsearch(customer_number, iso_country_code, part_number)

Search product catalog

Search product catalog using Ingram part numbers, vendor/manufacturer part numbers, customer part numbers or UPC. Use this endpoint to find the ingrampartnumber using vendorpartnumber or UPC.  - PartNumber field is capable of searching Ingram part numbers, vendor/manufacturer part numbers, customer part numbers or UPC.  *NOTE: isoCountryCode and customerNumber is mandatory.* 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: application
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CatalogApi(swagger_client.ApiClient(configuration))
customer_number = '20-222222' # str | Your unique Ingram Micro customer number (default to 20-222222)
iso_country_code = 'US' # str | 2 chars country code (default to US)
part_number = '1AQ821' # str | Part Number can be ingram part number or vendor part number or customer part number or UPC (default to 1AQ821)

try:
    # Search product catalog
    api_response = api_instance.get_v5_catalog_productsearch(customer_number, iso_country_code, part_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_v5_catalog_productsearch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_number** | **str**| Your unique Ingram Micro customer number | [default to 20-222222]
 **iso_country_code** | **str**| 2 chars country code | [default to US]
 **part_number** | **str**| Part Number can be ingram part number or vendor part number or customer part number or UPC | [default to 1AQ821]

### Return type

[**ProductSearchResponse**](ProductSearchResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multi_sku_price_and_stock**
> PriceAndAvailabilityResponse multi_sku_price_and_stock(body=body)

Find availability of upto 50 SKUs

Please use this end-point to find the price and availability of up to 50 SKUs while placing an order. This endpoint helps to confirm the details just prior to placing a real-time call.  This endpoint is not for refreshing the full catalog with availability and pricing information. We are applying rate-limits on this endpoint and continuous cyclical calls will start erroring out. Customers that perform this activity may lose access to the endpoint.  For the full catalog refresh, we can provide a Price and Inventory file in flat file format, which can be obtained through FTP download. Please contact your sales rep for details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: application
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CatalogApi(swagger_client.ApiClient(configuration))
body = swagger_client.PriceAndAvailabilityRequest() # PriceAndAvailabilityRequest |  (optional)

try:
    # Find availability of upto 50 SKUs
    api_response = api_instance.multi_sku_price_and_stock(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->multi_sku_price_and_stock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PriceAndAvailabilityRequest**](PriceAndAvailabilityRequest.md)|  | [optional] 

### Return type

[**PriceAndAvailabilityResponse**](PriceAndAvailabilityResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

