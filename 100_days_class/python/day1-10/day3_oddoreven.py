# Program to test if a number is odd or even using the modulo operator

number = int(input("Which number do you want to check?\n"))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"the number {number} is odd.")
