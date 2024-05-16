import random
import requests
from dotenv import load_dotenv
import os
from tkinter import *
from tkinter import simpledialog

load_dotenv()

CG_KEY = os.getenv('COIN_GECKO_API_KEY')

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

class KeyEntry(simpledialog.Dialog):

    def __init__(self, parent, title=None):
        self.result = None
        super().__init__(parent, title)

    def buttonbox(self):
        pass

    def body(self, master):

        master.configure(bg='black', highlightthickness=0, padx=30, pady=30)

        self.enter_label = Label(master, text='Enter Your API key for CoinGecko', bg='black', fg='orange', font=('Arial', 16, 'bold'))
        self.enter_sub_label = Label(master, text='- If a key has already been stored close the window\n'
                                                  '- To overwrite a key simply enter a new one\n'
                                                  '- Click "Enter Key" with an empty field to show your current key\n'
                                                  '- Make sure the field is clear before entering a new key', bg='black', fg='orange', font=('Arial', 11, 'italic'))
        self.enter_label.grid(column=0, row=0, pady=(10, 0), padx=10)
        self.enter_sub_label.grid(column=0, row=1, pady=(0, 10))

        self.enter_key = Entry(master, width=42, bg='orange', fg='black', font=('Arial', 14, 'italic'))
        self.enter_key.grid(column=0, row=3)

        self.enter_key_button = Button(master, text='Enter Key', bg='grey', fg='black', font=('Arial', 14, 'bold'), command=self.write_key_to_env)
        self.enter_key_button.grid(column=1, row=3, padx=(5, 0))

    def write_key_to_env(self):
        x = self.enter_key.get()

        if len(x) == 0:
            with open('.env', 'r') as file:
                x = file.read()
                x = x[21:]
                self.enter_key.config(bg='Yellow')
                self.enter_key.insert(0, f'Current Key: {x}')

        else:
            with open('.env', 'w') as file:
                file.write(f'COIN_GECKO_API_KEY = {x}')

            self.enter_key.delete(0, 'end')
            self.enter_key.config(bg='Green')
            self.enter_key.insert(0, 'Your Key Has Been Entered')






class CryptoWidget():

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

        self.open_key_entry()

        self.window.mainloop()

    def open_key_entry(self):
        popup_key_entry = KeyEntry(self.window, 'Key Entry')

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