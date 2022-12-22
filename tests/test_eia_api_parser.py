import pandas.core.series
import pytest

from lib.eia_api import EiaApiCaller, EiaApiParserSTEO, EiaApiParserPrices
from lib.api_calls_dicts import steo_calls, price_calls


class TestSTEOApiCall:
    def test_api_call_pass(self):
        key = 'world_production'
        query = steo_calls.get(key)
        response = EiaApiCaller(query).make_request()
        assert response.status_code == 200

    def test_api_call_fail(self):
        key = 'bad_call'
        query = 'https://api.eia.gov/v2/data/?frequency=monthly&data[0]=value&facets[seriesId][]=T3_STCHANGE_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000'
        assert EiaApiCaller(query).make_request() == None

    @pytest.fixture(scope='class')
    def parser(self):
        key = 'world_production'
        query = steo_calls.get(key)
        response = EiaApiCaller(query).make_request()
        parser = EiaApiParserSTEO(response)
        return parser

    def test_parser_returns_json_to_dict(self, parser):
        assert isinstance(parser.make_dict_from_json_response(), dict)

    def test_parser_returns_pandas_series(self, parser):
        assert isinstance(parser.parse_response_to_series(),
                          pandas.core.series.Series)
        pass

    def test_metadata_has_attributes(self, parser):
        metadata_fields = set(parser.eia_metadata._fields)
        keys = {"series_id", "frequency", "description", "units", "date_range"}

        assert metadata_fields & keys

class TestPricesApiCall:
    def test_api_call_pass(self):
        key = 'brent_spot_price'
        query = price_calls.get(key)
        response = EiaApiCaller(query).make_request()
        assert response.status_code == 200

    def test_api_call_fail(self):
        key = 'bad_call'
        query = 'https://api.eia.gov/v2/data/?frequency=monthly&data[0]=value&facets[seriesId][]=T3_STCHANGE_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000'
        assert EiaApiCaller(query).make_request() == None

    @pytest.fixture(scope='class')
    def parser(self):
        key = 'brent_spot_price'
        query = price_calls.get(key)
        response = EiaApiCaller(query).make_request()
        parser = EiaApiParserPrices(response)
        return parser

    def test_parser_returns_json_to_dict(self, parser):
        assert isinstance(parser.make_dict_from_json_response(), dict)

    def test_parser_returns_pandas_series(self, parser):
        assert isinstance(parser.parse_response_to_series(),
                          pandas.core.series.Series)
        pass

    def test_metadata_has_attributes(self, parser):
        metadata_fields = set(parser.eia_metadata._fields)
        keys = {"series_id", "frequency", "description", "units", "date_range"}

        assert metadata_fields & keys