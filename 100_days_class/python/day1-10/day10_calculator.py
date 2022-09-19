print("Welcome to the Calculator app")


def calc(first_number, operator, second_number):
    print("Calculating")
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number


first_number = int(input("First number?#\n "))
operator = input("Operator?#\n +\n -\n *\n /\n# ")
second_number = int(input("Second number?#n "))
print(calc(first_number, operator, second_number))


# fix this to use a dictionary for operator
