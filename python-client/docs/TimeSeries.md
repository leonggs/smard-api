# TimeSeries


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_data** | [**TimeSeriesMetaData**](TimeSeriesMetaData.md) |  | [optional] 
**series** | **List[List[float]]** |  | [optional] 

## Example

```python
from deutschland.smard.models.time_series import TimeSeries

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeries from a JSON string
time_series_instance = TimeSeries.from_json(json)
# print the JSON string representation of the object
print TimeSeries.to_json()

# convert the object into a dict
time_series_dict = time_series_instance.to_dict()
# create an instance of TimeSeries from a dict
time_series_form_dict = time_series.from_dict(time_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


