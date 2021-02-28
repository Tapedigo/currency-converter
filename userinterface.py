def WelcomeMessage():
    print("Welcome to my currency conversion app!")

def Input():
    Usd = input('What amount would you like to convert(USD)? ')
    print(Usd)
    if Usd == int:
        ValueError('Please enter an integer')
    else:
        input("""What currency would you like to convert to?
1. GDP \n2. EUR \n""")

Input()