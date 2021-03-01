import requests

url ='https://v6.exchangerate-api.com/v6/af370279909b3852fbc7252f/latest/USD'
def AppCaller():
    response = requests.get(url)
    data = response.json()
    