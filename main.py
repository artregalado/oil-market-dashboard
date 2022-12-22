import time

import matplotlib.pyplot as plt

from lib.api_calls_dicts import steo_calls, price_calls
from lib.eia_api import EiaApiCaller, EiaApiParserSTEO, EiaApiParserPrices

start = time.time()

for key in steo_calls.keys():
    api_query = steo_calls.get(key)
    response = EiaApiCaller(api_query).make_request()
    parser = EiaApiParserSTEO(response)
    data = parser.parse_response_to_series()
    print(parser.eia_metadata)
    print(data.index.freq.freqstr)
    print(data)
    print("="*80)
    data.plot()
    plt.title(key)
    plt.show()
    time.sleep(1)

for key in price_calls.keys():
    api_query = price_calls.get(key)
    response = EiaApiCaller(api_query).make_request()
    parser = EiaApiParserPrices(response)
    data = parser.parse_response_to_series()
    print(parser.eia_metadata)
    print(data.index.freq.freqstr)
    print(data)
    print("="*80)
    data.plot()
    plt.title(key)
    plt.show()
    time.sleep(1)

end = time.time()
print(f'It took {end - start} seconds!')