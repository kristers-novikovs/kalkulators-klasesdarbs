"""Calculator with 4 functions"""

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    
    try:
        return a / b
    except ZeroDivisionError as e:
        return"One cannot divide with 0."

def multiplication(a, b):
    return a * b

def main():
    number1= float(input("Number:"))
    number2= float(input("Number:"))

    print(""""
        1 - addition
        2 - subtraction
        3 - division
        4 - multiplication """)

    method = int(input("Method:"))
    if method == 1:
        print(addition(number1, number2))
    elif method == 2:
        print(subtraction(number1, number2))
    elif method == 3:
        print(division(number1, number2))
    elif method == 4:
        print(multiplication(number1, number2))
    else:
        print("One does not have such method.")


if __name__ == "__main__":
    main()
