# PriceAndAvailabilityResponseServiceresponsePriceandstockresponseDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**itemstatus** | **str** | SUCCESS or FAILED | [optional] 
**statusmessage** | **str** | Description of itemstatus | [optional] 
**ingrampartnumber** | **str** | Ingram Micro part number | [optional] 
**vendorpartnumber** | **str** | Manufacturer/Vendor part number | [optional] 
**globalskuid** | **str** |  | [optional] 
**customerprice** | **float** | Customer specific price for the product, excluding taxes | [optional] 
**partdescription1** | **str** | Product description part 1 | [optional] 
**partdescription2** | **str** | Product description part 2 | [optional] 
**vendornumber** | **str** |  | [optional] 
**vendorname** | **str** | Name of the vendor | [optional] 
**cpucode** | **str** |  | [optional] 
**_class** | **str** | Ingram Micro assigned product classification -  A-Stocked product in all IM warehouses, B-Limited stock in IM warehouses, C-Stocked in fewer wareshouses, D-Ingram discontinued, E-Planned to be phased out as per the vendor, F-Carried for specific customer as per the contract, N-New SKU, O-Discontinued to be liquidated, S-Order for specialized demand, V-Discontinued by vendor, X-Direct Ship products from vendor | [optional] 
**skustatus** | **str** | Identifies if the SKU has been discontinued. | [optional] 
**mediacpu** | **str** |  | [optional] 
**categorysubcategory** | **str** |  | [optional] 
**retailprice** | **float** |  | [optional] 
**newmedia** | **str** |  | [optional] 
**enduserrequired** | **str** | Y - End user required N - Not required End user | [optional] 
**backorderflag** | **str** | Y- Allow Backorder Flag N- Not allowed | [optional] 
**skuauthorized** | **str** |  | [optional] 
**extendedvendorpartnumber** | **str** |  | [optional] 
**warehousedetails** | [**list[WarehouseListType]**](WarehouseListType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

