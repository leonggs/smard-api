# coding: utf-8

"""
    Bundesnetzagentur Strommarktdaten

    Bundesnetzagentur Strommarktdaten

    The version of the OpenAPI document: 0.0.1
    Contact: kontakt@bund.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from deutschland.smard.models.time_series2_series_inner_values_inner_versions_inner import TimeSeries2SeriesInnerValuesInnerVersionsInner  # noqa: E501

class TestTimeSeries2SeriesInnerValuesInnerVersionsInner(unittest.TestCase):
    """TimeSeries2SeriesInnerValuesInnerVersionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeSeries2SeriesInnerValuesInnerVersionsInner:
        """Test TimeSeries2SeriesInnerValuesInnerVersionsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeSeries2SeriesInnerValuesInnerVersionsInner`
        """
        model = TimeSeries2SeriesInnerValuesInnerVersionsInner()  # noqa: E501
        if include_optional:
            return TimeSeries2SeriesInnerValuesInnerVersionsInner(
                value = 1.337,
                name = None
            )
        else:
            return TimeSeries2SeriesInnerValuesInnerVersionsInner(
        )
        """

    def testTimeSeries2SeriesInnerValuesInnerVersionsInner(self):
        """Test TimeSeries2SeriesInnerValuesInnerVersionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
