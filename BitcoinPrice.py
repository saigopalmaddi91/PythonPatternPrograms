import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

bitcoin_info = response.json()  # it gives python dic object

print('Bitcoin price as of', bitcoin_info['time']['updated'])
print('1 BTC = $', bitcoin_info['bpi']['USD']['rate'])