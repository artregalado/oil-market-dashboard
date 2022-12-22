steo_calls = {
    'world_production': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PAPR_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'world_consumption': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=PATC_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000',
    'world_net_inventories': 'https://api.eia.gov/v2/steo/data/?frequency=monthly&data[0]=value&facets[seriesId][]=T3_STCHANGE_WORLD&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000'
}


price_calls = {'brent_price':'https://api.eia.gov/v2/petroleum/pri/spt/data/?frequency=weekly&data[0]=value&facets[series][]=RBRTE&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
}

