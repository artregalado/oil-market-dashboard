import pandas.core.series
import pytest

from lib.eia_api import EiaApiCaller, EiaApiParserSTEO, EiaApiParserPrices
from lib.api_calls_dicts import steo_calls, price_calls


class TestSTEOApiCall:
    def test_api_call_pass(self):
        key = 'total_world_production'
        query = steo_calls.get(key)
        response = EiaApiCaller(query).make_request()
        assert response.status_code == 200

    def test_api_call_fail(self):
        key = 'bad_call'
        query = 'https://api.eia.gov/v2/data/?frequency=monthly&data[0]=value&facets[seriesId][]=T3_STCHANGE_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000'
        assert EiaApiCaller(query).make_request() == None

    @pytest.fixture(scope='class')
    def parser(self):
        key = 'total_world_production'
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
        key = 'brent_spot_weekly_price'
        query = price_calls.get(key)
        response = EiaApiCaller(query).make_request()
        assert response.status_code == 200

    def test_api_call_fail(self):
        key = 'bad_call'
        query = 'https://api.eia.gov/v2/data/?frequency=monthly&data[0]=value&facets[seriesId][]=T3_STCHANGE_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000'
        assert EiaApiCaller(query).make_request() == None



class TestPricesApiParser:

    @pytest.fixture(scope='class')
    def parser(self):
        key = 'brent_spot_weekly_price'
        query = price_calls.get(key)
        response = EiaApiCaller(query).make_request()
        parser = EiaApiParserPrices(response)
        return parser

    def test_parser_returns_json_to_dict(self, parser):
        assert isinstance(parser.make_dict_from_json_response(), dict)

    def test_parser_returns_pandas_series(self, parser):
        assert isinstance(parser.parse_response_to_series(),
                          pandas.core.series.Series)

    def test_metadata_has_attributes(self, parser):
        metadata_fields = set(parser.eia_metadata._fields)
        keys = {"series_id", "frequency", "description", "units", "date_range"}
        assert metadata_fields & keys

    @pytest.fixture(scope='class')
    def parsers_list(self):
        parsers = []
        for key in price_calls.keys():
            query = price_calls.get(key)
            response = EiaApiCaller(query).make_request()
            parser = EiaApiParserPrices(response)
            parsers.append(parser)
        return parsers

    def test_series_index_of_correct_time_period(self, parsers_list):
        for parser in parsers_list:
            series = parser.parse_response_to_series()

            if parser.eia_metadata.frequency == "annual":
                assert series.index.freq.freqstr == "A-DEC"
            elif parser.eia_metadata.frequency == "monthly":
                assert series.index.freq.freqstr == "M"
            elif parser.eia_metadata.frequency == "weekly":
                assert series.index.freq.freqstr == "W-FRI"
            else:
                assert series.index.freq.freqstr == "D"
