import CurrencyAppCaller


def WelcomeMessage():
    print("Welcome to my currency conversion app!")

def UserInput():
    Usd = input('What amount would you like to convert(USD)? ')
    if Usd != float or int:
        ValueError('Please enter an number')
    

WelcomeMessage()

while True:
    input_of_user = input("What amount would you like to convert(USD)? ")
    
    if input_of_user == 'quit'.lower():
        break
    else:
        Currency = input("What currency would you like to convert to? ")
        converter = CurrencyAppCaller.CurrencyCoverter(url = 'https://v6.exchangerate-api.com/v6/af370279909b3852fbc7252f/latest/USD')
        print(converter.Convert(float(input_of_user), 'USD', Currency.upper()))
        continue
    