def calculate():
    # Prompt for user input
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    # Addition
    print("{} + {} = ".format(a, b))
    print(a + b)

    # Subtraction
    print("{} - {} = ".format(a, b))
    print(a - b)

    # Multiplication
    print("{} * {} = ".format(a, b))
    print(a * b)

    # Division
    print('{} / {} = '.format(a, b))
    print(a / b)

def again():
    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

# Call calculate() outside of the function
calculate()