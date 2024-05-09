superscript_num = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

def get_one_number():
    num = int(input("Enter a number: "))
    return num

def get_two_numbers():
    num1 = int(input(("Enter first number: ")))
    num2 = int(input(("Enter second number: ")))
    return num1, num2

def addition():
    num1, num2 = get_two_numbers()
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

def subtraction():
    num1, num2 = get_two_numbers()
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

def multiplication():
    num1, num2 = get_two_numbers()
    result = num1 * num2
    print(f"{num1} × {num2} = {result}")

def division():
    num1, num2 = get_two_numbers()
    result = num1 / num2
    print(f"{num1} ÷ {num2} = {result}")

def square():
    num = get_one_number()
    result = num ** 2
    print(f"{num}² = {result}")

def exponent():
    base = int(input("Enter base: "))
    power = int(input("Enter power: "))
    result = base ** power
    print(f"{base}{str(power).translate(superscript_num)} = {result}")

def square_root():
    num = get_one_number()
    if num < 0:
        print("Square root of negative number is not real")
    elif num == 0:
        print(0)
    x = num
    y = (x + 1 ) / 2
    while y < x:
        x = y
        y = (x + num / x) / 2
    print(f"√({num}) = {x}")

def factorial():
    num = get_one_number()
    original_num = num
    factorial = 1

    while num > 0:
        factorial *= num
        num -= 1

    print(f"{original_num}! = {factorial}")
    

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