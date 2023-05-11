#!/usr/bin

""" Simple program that subtracts two numbers and prints the result. """

def subtract_numbers(num1, num2):
    """ Subtracts two numbers and prints:
        - POSITIVE, if the result is grater than zero,
        - NEGATIVE, if the result is lower than zero,
        - ZERO, if the result is equal to zero.
    """
    sub = num1 - num2

    if sub > 0:
        print("POSITIVE")
    elif sub < 0:
        print("NEGATIVE")
    else:
        print("ZERO")

def main():
    """ Prompts the user to give two numbers and
        calls subtract_numbers to display the result. 
    """
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        subtract_numbers(num1, num2)

        _exit = input("Exit? (y/n)").lower()
        if _exit == 'y':
            print("Quiting...")
            break

if __name__ == "__main__":
    main()
