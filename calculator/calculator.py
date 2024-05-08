def addition():
    num1 = int(input(("Enter first number: ")))
    num2 = int(input(("Enter second number: ")))
    result = num1 + num2
    print(result)

def subtraction():
    num1 = int(input(("Enter first number: ")))
    num2 = int(input(("Enter second number: ")))
    result = num1 - num2
    print(result)

def multiplication():
    num1 = int(input(("Enter first number: ")))
    num2 = int(input(("Enter second number: ")))
    result = num1 * num2
    print(result)

def division():
    num1 = int(input(("Enter first number: ")))
    num2 = int(input(("Enter second number: ")))
    result = num1 / num2
    print(result)

def square():
    num = int(input("Enter number: "))
    result = num ** 2
    print(result)

def exponent():
    base = int(input("Enter base: "))
    power = int(input("Enter power: "))
    result = base ** power
    print(result)

def square_root():
    num = int(input("Enter a number: "))
    if num < 0:
        print("Square root of negative number is not real")
    elif num == 0:
        print(0)
    x = num
    y = (x + 1 ) // 2
    while y < x:
        x = y
        y = (x + num // x) // 2
    print(x)

def factorial():
    num = int(input("Enter a number: "))
    factorial = 1

    while num > 0:
        factorial *= num
        num -= 1

    print(factorial)
    

def main():
    while True:
        print("\n")
        print("*" * 70)
        print("Calulator | Enter your operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square")
        print("6. Exponent")
        print("7. Square Root")
        print("8. Factorial")
        print("9. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                addition()
            case '2':
                subtraction()
            case '3':
                multiplication()
            case '4':
                division()
            case '5':
                square()
            case '6':
                exponent()
            case '7':
                square_root()
            case '8':
                factorial()
            case '9':
                print("Thank you, have a great day!")
            case _:
                print("Invalid Choice!!")
        print("*" * 70)

if __name__ == "__main__":
    main()