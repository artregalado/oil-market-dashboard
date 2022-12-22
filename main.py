import pandas as pd
import matplotlib.pyplot as plt

from lib.api_calls_dicts import steo_calls
from lib.eia_api_parser import EiaApiCaller, EiaApiParserSTEO

api_query = steo_calls.get('world_production')
response = EiaApiCaller(api_query).make_request()
parser = EiaApiParserSTEO(response)
data = parser.parse_response_to_series()
data.plot()
plt.show()
