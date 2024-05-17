```
      ___                         ___           ___           ___           ___           ___           ___     
     /\__\                       /\  \         /\__\         /\  \         /\__\         /\  \         /\  \    
    /:/ _/_         ___          \:\  \       /:/ _/_       /::\  \       /:/ _/_        \:\  \       |::\  \   
   /:/ /\__\       /\__\          \:\  \     /:/ /\__\     /:/\:\__\     /:/ /\__\        \:\  \      |:|:\  \  
  /:/ /:/ _/_     /:/  /      ___ /::\  \   /:/ /:/ _/_   /:/ /:/  /    /:/ /:/ _/_   ___  \:\  \   __|:|\:\  \ 
 /:/_/:/ /\__\   /:/__/      /\  /:/\:\__\ /:/_/:/ /\__\ /:/_/:/__/___ /:/_/:/ /\__\ /\  \  \:\__\ /::::|_\:\__\
 \:\/:/ /:/  /  /::\  \      \:\/:/  \/__/ \:\/:/ /:/  / \:\/:::::/  / \:\/:/ /:/  / \:\  \ /:/  / \:\~~\  \/__/
  \::/_/:/  /  /:/\:\  \      \::/__/       \::/_/:/  /   \::/~~/~~~~   \::/_/:/  /   \:\  /:/  /   \:\  \      
   \:\/:/  /   \/__\:\  \      \:\  \        \:\/:/  /     \:\~~\        \:\/:/  /     \:\/:/  /     \:\  \     
    \::/  /         \:\__\      \:\__\        \::/  /       \:\__\        \::/  /       \::/  /       \:\__\    
     \/__/           \/__/       \/__/         \/__/         \/__/         \/__/         \/__/         \/__/    

```

# Ethereum Ticker +

*Note: CoinGecko might take a moment to update the price, so resist the urge to refresh too frequently. It updates around every 20-40 seconds.*

*Note2: The .exe version does work, but like 99% for sure will get flagged by antivirus, after clearing it
the few windows machines I have tested it on work great, so pick your poison I guess*

## Beta Release 1.0

A neat little widget for your desktop, keeping you updated on Ethereum's price.

*This app is available as an executable, so you don't even need Python installed. If you give it a whirl, 
let me know how it goes—I've only been able to test it on my own machines. The executable is tucked away in 
the "Crypto Ticker +" folder of the repo, created using "auto-py-to-exe." It wasn't as smooth sailing as 
I expected, but still fairly intuitive.*

Alternatively, you can install the dependencies and run the script directly. Both options are available in the repo.

### Instructions:

1. The initial pop-up prompts you to enter your API key. If you've already done this, just close it and move to step 3.\
   **A.** Paste your CoinGecko API key during the first run—it's a one-time thing.\
   **B.** Click "Enter Key" with an empty field to check your current key.\
   **C.** Made a mistake? Want to switch keys? No problem, just re-enter it.\
   **D.** Only one key can be stored at a time; there's no need for more. Entering a new key overwrites the existing one.

2. Once you've entered the key, or if it's already stored, close the pop-up.
3. Use the refresh button to load the price initially. Hit it again whenever you want to update.\
   **A.** It might seem like a hassle initially, but it saves you from purchasing a key.\
   **B.** CoinGecko's price updates can be slow; the color of the price changes on each refresh to signal success.\
   **C.** Spamming the button won't speed up the process due to CoinGecko's update frequency.

## Features

- Key stored securely in .env for easy updating.
- Check your stored key by clicking "Enter Key" with an empty field.
- Compact window/widget fits seamlessly on your screen.
- Refresh button ensures you have the latest price without wasting API calls.
- Price text color changes on refresh for visual confirmation.

## API key

You'll need your own API key from CoinGecko to use this. They offer a free tier, which provides 10,000 calls per month or 30 per minute.

[Get your CoinGecko API key](https://www.coingecko.com/en/api)

## Whats Coming

- More sanding of the edges, make things look nicer and spiff up error handling (currently none).
- Themes that can easily be changed.
- Settings to change CryptoCurrency.
- Settings to change fiat currency.

## When ? 

Right now I will be working on this pretty frequently, if things change I will update this.



