import urllib.request
import json
class CurrencyCoverter:
    def __init__(self, url):
        request = urllib.request.Request(url, headers={'User-Agent': 'Currency Converter'})
        data = urllib.request.urlopen(request).read()
        data = json.loads(data.decode('utf-8'))
        self.conversion_rates = data['conversion_rates']
    
    def Convert(self, amount, from_money, to_money):
        original_amount = amount
        if from_money.upper() != 'USD':
            amount = amount / self.conversion_rates[from_money.upper()]
        elif from_money.upper() == 'USD':
            return str(original_amount) + " ("+ from_money + ") is equal to " + (str(amount * self.conversion_rates[to_money])) + " ("+ to_money + ")"
        else:
            return original_amount, amount * self.conversion_rates[to_money]
url = 'https://v6.exchangerate-api.com/v6/af370279909b3852fbc7252f/latest/USD'
    
converter = CurrencyCoverter(url)

