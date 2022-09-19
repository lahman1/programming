
def prime_checker(number):
    if n % 2 == 0 and n != 2:
        print("It's not a prime number")
    elif n % 3 == 0 and n != 3:
        print("It's not a prime number")
    elif n % 5 == 0 and n != 5:
        print("It's not a prime number")
    elif n % 7 == 0 and n != 7:
        print("It's not a prime number")
    else:
        print("It's a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
