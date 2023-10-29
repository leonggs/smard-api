# TimeSeriesMetaData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | [optional] 
**created** | **int** |  | [optional] 

## Example

```python
from deutschland.smard.models.time_series_meta_data import TimeSeriesMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeriesMetaData from a JSON string
time_series_meta_data_instance = TimeSeriesMetaData.from_json(json)
# print the JSON string representation of the object
print TimeSeriesMetaData.to_json()

# convert the object into a dict
time_series_meta_data_dict = time_series_meta_data_instance.to_dict()
# create an instance of TimeSeriesMetaData from a dict
time_series_meta_data_form_dict = time_series_meta_data.from_dict(time_series_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


