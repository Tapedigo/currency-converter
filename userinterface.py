import CurrencyAppCaller


def WelcomeMessage():
    print("Welcome to my currency conversion app!")

def Input():
    Usd = input('What amount would you like to convert(USD)? ')
    if Usd != float or int:
        ValueError('Please enter an number')
    else:
        Currency = input("What currency would you like to convert to?")
        converter = CurrencyAppCaller.CurrencyCoverter(url = 'https://v6.exchangerate-api.com/v6/af370279909b3852fbc7252f/latest/USD')
        print(converter.Convert(Usd, 'USD', Currency.upper()))
WelcomeMessage()

while True:
    UserInput = input
    Input()
    if input == 'quit'.lower :
        break
