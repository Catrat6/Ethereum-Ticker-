import requests
from dotenv import load_dotenv
import os
import pprint
from tkinter import *

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

class CryptoWidget:

    def __init__(self):
        self.window = Tk()
        self.window.title('Eth Ticker +')
        self.window.config(bg='black', pady=30, padx=30)

        self.display = Canvas(height=150, width=400, bg='black')
        self.price_text = self.display.create_text(200, 75, text='This is text', fill='orange', font=('Arial', 16, 'bold'), width=130)
        self.display.grid(row=0, column=0)





        self.window.mainloop()




CryptoWidget()