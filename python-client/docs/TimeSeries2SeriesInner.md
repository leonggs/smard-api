# TimeSeries2SeriesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[TimeSeries2SeriesInnerValuesInner]**](TimeSeries2SeriesInnerValuesInner.md) |  | [optional] 

## Example

```python
from deutschland.smard.models.time_series2_series_inner import TimeSeries2SeriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeries2SeriesInner from a JSON string
time_series2_series_inner_instance = TimeSeries2SeriesInner.from_json(json)
# print the JSON string representation of the object
print TimeSeries2SeriesInner.to_json()

# convert the object into a dict
time_series2_series_inner_dict = time_series2_series_inner_instance.to_dict()
# create an instance of TimeSeries2SeriesInner from a dict
time_series2_series_inner_form_dict = time_series2_series_inner.from_dict(time_series2_series_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


