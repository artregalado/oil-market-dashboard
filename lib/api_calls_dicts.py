steo_calls = {
    # Production data series
    'total_world_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'oecd_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_OECD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'usa_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_US&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'canada_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_CA&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'mex_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_MX&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'other_oecd_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_OTHEROECD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'non_oecd_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_NONOECD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'opec_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_OPEC&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'eurasia_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_FSU&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'china_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_CH&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'other_non_oecd_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_OTHER_NONOECD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'total_non_opec_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_NONOPEC&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    # Consumption data series
    'total_world_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'oecd_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_OECD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'usa50_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_US&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'usterreitories_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_UST&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'canada_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_CA&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'europe_oecd_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_OECD_EUROPE&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'japan_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_JA&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'other_oecd_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_OTHER_OECD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'non_oecd_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_NON_OECD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'eurasia_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_FSU&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'europe_non_oecd_consumtpion': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_NONOECD_EUROPE&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'china_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_CH&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'other_asia_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_OTHER_ASIA&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'other_non_oecd_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_OTHER_NONOECD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    # Inventory changes data series
    'total_stock_net_draw': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=T3_STCHANGE_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'usa_commercial_inventories': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PASC_US&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'oecd_commercial_inventories': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PASC_OECD_T3&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000'}


price_calls = {'brent_spot_price':'https://api.eia.gov/v2/petroleum/pri/spt/data/?frequency=weekly&data[0]=value&facets[series][]=RBRTE&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
               'wti_spot_price': 'https://api.eia.gov/v2/petroleum/pri/spt/data/?frequency=weekly&data[0]=value&facets[product][]=EPCWTI&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000'}

