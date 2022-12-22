import pandas as pd
import matplotlib.pyplot as plt

from lib.api_calls_dicts import steo_calls, price_calls
from lib.eia_api import EiaApiCaller, EiaApiParserSTEO, EiaApiParserPrices

for key in steo_calls.keys():
    api_query = steo_calls.get(key)
    response = EiaApiCaller(api_query).make_request()
    parser = EiaApiParserSTEO(response)
    data = parser.parse_response_to_series()

    data.plot()
    plt.title(key)
    plt.show()

for key in price_calls.keys():
    api_query = price_calls.get(key)
    response = EiaApiCaller(api_query).make_request()
    parser = EiaApiParserPrices(response)
    data = parser.parse_response_to_series()
    data.plot()
    plt.show()
