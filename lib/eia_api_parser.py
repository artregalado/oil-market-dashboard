from dataclasses import dataclass
from collections import namedtuple
import requests
from requests.exceptions import HTTPError
import json
import pandas as pd

@dataclass
class EiaApiCaller:
    api_call: str
    api_key: str = 'WgEuHKiqOyQwlmARUIbUg8ZR3Eh1sXQYkT7oXJia'

    def make_request(self) -> requests.Response:
        payload = {'api_key': self.api_key}
        try:
            response = requests.get(self.api_call, params=payload)
            response.raise_for_status()
            return response
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')

class EiaApiParserSTEO:
    """
    The parser is assumming the request is to Caller returns 1 data series.
    The parser will not work with calls that return more than 1
    data series.

    It also only works with monthly series
    """

    def __init__(self, response):

        self.response: requests.Response = response

    def make_dict_from_json_response(self) -> str:
        response = self.response
        return json.loads(response.text)

    def write_json_response_to_file(self, filename: str) -> None:
        response = self.make_dict_from_json_response()
        with open(filename, 'w') as f:
            f.write(json.dumps(response, indent=4))

    @property
    def date_format_for_metadata(self):
        response = self.make_dict_from_json_response()
        frequency = response['response']['frequency']

        if frequency == "monthly":
            return "%Y-%m"
        elif frequency == "daily":
            return "%Y-%m-%d"
        elif frequency == "annual":
            return "%Y"
        elif frequency == "weekly":
            return "%Y-%m-%w"
        else:
            return "Cannot determine date frequency"

    def parse_response_to_series(self) -> pd.Series:
        response = self.make_dict_from_json_response()
        data_list = response['response']['data']

        values = []
        dates = []
        for t in range(len(data_list)):
            values.append(data_list[t]['value'])
            dates.append(data_list[t]['period'])
        dates = map(pd.Period, dates)

        name = data_list[0]['seriesId']

        series = pd.Series(values, index=list(dates), name=name)
        return series

    @property
    def eia_metadata(self):
        response = self.make_dict_from_json_response()
        data_series = self.parse_response_to_series()

        first_point = response['response']['data'][0]

        Metadata = namedtuple("Metadata",
                              'series_id frequency description units date_range')

        series_id = first_point['seriesId']
        frequency = response['response']['frequency']
        description = first_point['seriesDescription']
        units = first_point['unit']
        min_date = data_series.index.min().to_timestamp().strftime(
            self.date_format_for_metadata)
        max_date = data_series.index.max().to_timestamp().strftime(
            self.date_format_for_metadata)
        date_range = str(f"from {min_date} to {max_date}")

        return Metadata(series_id, frequency,
                        description, units,
                        date_range)
