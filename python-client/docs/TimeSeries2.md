# TimeSeries2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_data** | [**TimeSeriesMetaData**](TimeSeriesMetaData.md) |  | [optional] 
**series** | [**List[TimeSeries2SeriesInner]**](TimeSeries2SeriesInner.md) |  | [optional] 

## Example

```python
from deutschland.smard.models.time_series2 import TimeSeries2

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeries2 from a JSON string
time_series2_instance = TimeSeries2.from_json(json)
# print the JSON string representation of the object
print TimeSeries2.to_json()

# convert the object into a dict
time_series2_dict = time_series2_instance.to_dict()
# create an instance of TimeSeries2 from a dict
time_series2_form_dict = time_series2.from_dict(time_series2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


