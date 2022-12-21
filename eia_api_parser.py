from dataclasses import dataclass
from collections import namedtuple
import requests
import json
import pandas as pd
import re

crude_api_calls = {
    'world_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'world_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'world_net_inventories': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=T3_STCHANGE_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000'}


@dataclass
class EieApiCaller:
    api_key: str = 'WgEuHKiqOyQwlmARUIbUg8ZR3Eh1sXQYkT7oXJia'


@dataclass
class EiaApiParser:
    """
    The parser is assumming the request is to collect 1 data series.
    Consequently the parser will not work with calls that return more than 1
    data series.

    It also only works with monthly series
    """
    api_call: str
    series_alias: str
    api_key: str = 'WgEuHKiqOyQwlmARUIbUg8ZR3Eh1sXQYkT7oXJia'

    def make_request(self) -> requests.Response:
        payload = {'api_key': self.api_key}
        return requests.get(self.api_call, params=payload)

    @property
    def get_raw_response(self) -> str:
        response = self.make_request()
        if response.status_code == requests.codes.ok:
            return json.loads(response.text)
        else:
            response.raise_for_status()

    @property
    def response_status(self) -> str:
        response = self.make_request()
        code = response.status_code
        reason = response.reason
        return f"Status code: {code} {reason} "

    def write_json_response_to_file(self, filename: str) -> None:
        response = self.get_raw_response
        with open(filename, 'w') as f:
            f.write(json.dumps(response, indent=4))

    @property
    def date_format_for_metadata(self):
        response = self.get_raw_response
        frequency = response['response']['frequency']

        if frequency == "monthly":
            return "%Y-%m"
        elif frequency == "daily":
            return "%Y-%m-%d"
        elif frequency == "annual":
            return"%Y"
        elif frequency == "weekly":
            return "%Y-%m-%w"
        else:
            return "Cannot determine date frequency"


    def parse_response_to_series(self) -> pd.Series:
        response = self.get_raw_response
        data_list = response['response']['data']

        values = []
        dates = []
        for t in range(len(data_list)):
            values.append(data_list[t]['value'])
            dates.append(data_list[t]['period'])
        dates = map(pd.Period, dates)

        series = pd.Series(values, index=list(dates), name=self.series_alias)
        return series

    @property
    def eia_metadata(self):
        response = self.get_raw_response
        data_series = self.parse_response_to_series()

        first_point = response['response']['data'][0]

        Metadata = namedtuple("Metadata",
                              'series_id frequency description units date_range')

        series_id = first_point['seriesId']
        frequency = response['response']['frequency']
        description = first_point['seriesDescription']
        units = first_point['unit']
        min_date = data_series.index.min().to_timestamp().strftime(self.date_format_for_metadata)
        max_date = data_series.index.max().to_timestamp().strftime(self.date_format_for_metadata)
        date_range = str(f"from {min_date} to {max_date}")

        return Metadata(series_id, frequency,
                        description, units,
                        date_range)


api_call = crude_api_calls.get('world_production')
series_alias = 'Total World Production'
call = EiaApiParser(api_call, series_alias)
data = call.parse_response_to_series()
metadata = call.eia_metadata


