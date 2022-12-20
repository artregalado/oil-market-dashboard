from dataclasses import dataclass
import requests
import json
import pandas as pd

crude_api_calls = {
    'world_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'world_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'world_net_inventories': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=T3_STCHANGE_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000'}


@dataclass
class EiaApiParser:
    api_call: str
    series_name: str
    api_key: str = 'WgEuHKiqOyQwlmARUIbUg8ZR3Eh1sXQYkT7oXJia'

    def make_request(self) -> requests.Response:
        payload = {'api_key': self.api_key}
        return requests.get(self.api_call, params=payload)

    def get_raw_response(self) -> str:
        response = self.make_request()
        if response.status_code == requests.codes.ok:
            return json.loads(response.text)
        else:
            response.raise_for_status()

    def parse_response_to_series(self) -> pd.Series:
        response = self.get_raw_response()
        series = response['response']['data']
        # TODO: Parse response and make data series in pandas

        return series

    def write_json_response_to_file(self, filename: str) -> None:
        response = self.get_raw_response()
        with open(filename, 'w') as f:
            f.write(json.dumps(response, indent=4))


api_call = 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000'
series_name = 'Total World Production'
call = EiaApiParser(api_call, series_name)
data = call.parse_response_to_series()
call.write_json_response_to_file(filename='test_call.json')
