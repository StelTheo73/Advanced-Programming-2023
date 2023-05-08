#!/usr/bin

def subtract_numbers(num1, num2):
    sub = num1 - num2

    if sub > 0:
        print("POSITIVE")
    elif sub < 0:
        print("NEGATIVE")
    else:
        print("ZERO")

def main():
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
