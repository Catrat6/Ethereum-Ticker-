import random

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

TEXT_COLORS = [
    "#ff6eff", "#ff4d4d", "#ffaa1d", "#39ff14", "#15f4ee",
    "#ff00ff", "#00ffff", "#ffff00", "#00ff00", "#ff0000"
]

class CryptoWidget:

    def __init__(self):
        self.window = Tk()
        self.window.title('Eth Ticker +')
        self.window.config(bg='black', pady=20, padx=20)

        self.info_label = Label(text='Ethereum Price: ', fg='orange', bg='black', font=('Arial', 14, 'italic'))
        self.info_label.grid(row=0, column=0, pady=5)

        refresh_img = PhotoImage(file='refresh.png')
        self.refresh_button = Button(image=refresh_img, highlightthickness=0, bg='grey', fg='orange', command=self.update_price)
        self.refresh_button.grid(row=0, column=2, pady=10)

        self.display = Canvas(height=150, width=400, bg='black', highlightthickness=2, highlightbackground='orange')
        self.price_text = self.display.create_text(200, 75, text='Refresh for Price', fill='orange', font=('Arial', 16, 'bold'), width=380)
        self.display.grid(row=1, column=0, columnspan=3)

        self.window.mainloop()

    def change_price(self):
        call = requests.get(CG_URL_single_coin, headers=headers, params=parameters_single)
        call.raise_for_status()
        data = call.json()
        price = data['ethereum']['usd']
        self.display.itemconfig(self.price_text, text=f'{price}', fill=random.choice(TEXT_COLORS), font=('Arial', 42, 'italic'))
        print(data)

    def update_price(self):
        self.window.after(1000, self.change_price())

CryptoWidget()