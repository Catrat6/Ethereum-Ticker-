import requests
from dotenv import load_dotenv
import os
import pprint

load_dotenv()

CG_KEY = os.getenv('coin_gecko_api_key')

path_coin = 'ethereum'

CG_URL_single_coin = 'https://api.coingecko.com/api/v3/simple/price'
CG_URL_coin_list = 'https://api.coingecko.com/api/v3/coins/list'
CG_URL_coin_data = f'https://api.coingecko.com/api/v3/coins/{path_coin}'


headers = {'accept': 'application/json'}

parameters_single = {
    'ids': 'ethereum',
    'vs_currencies': 'usd',
    'x_cg_demo_api_key': CG_KEY
}

parameters_list = {
    'include_platform': 'True'
}

parameters_data = {
    'market_data': 'true',
    'localization': 'false',
    'tickers': 'false',
    'community_data': 'false',
    'developer_data': 'false',
    'sparkline': 'false'
}


call = requests.get(CG_URL_coin_data, headers=headers, params=parameters_data)
call.raise_for_status()
x = call.json()

pprint.pp(x['market_data']['current_price']['usd'])




