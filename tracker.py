from urllib import response
import requests
import constants
from binance.client import Client
import time

client = Client(constants.binance_api_key, constants.binance_secret)

def get_prices():
    coins = ["BTC", "ETH", "MATIC"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }

    return data

def health_factor():
    btc_raw_price = client.get_avg_price(symbol='BTCUSDC')
    eth_raw_price = client.get_avg_price(symbol='ETHUSDC')
    matic_raw_price = client.get_avg_price(symbol='MATICUSDT')

    btc_price = float(btc_raw_price['price'])
    eth_price = float(eth_raw_price['price'])
    matic_price = float(matic_raw_price['price'])

    matic_borrow = x
    USDC_borrow = x
    ETH_borrow = x
    BTC_borrow = x
    DAI_borrow = x #add values as per AAVE

    amt_btc = 31.58
    liquidation_threshold = .75
    amt_current_borrows = round((btc_price*BTC_borrow) + (eth_price*ETH_borrow) + (matic_price*matic_borrow) + USDC_borrow + DAI_borrow,2)

    health_factor_print = ((btc_price/eth_price)*amt_btc*liquidation_threshold)/(amt_current_borrows/eth_price)
    return health_factor_print

    # data = requests.get('https://aave-api-v2.aave.com/data/tvl/')
    # if response.status_code == 200:
    # return data
if __name__ == "__main__":
    print(health_factor())


