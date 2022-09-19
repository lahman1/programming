# Password generator program
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
           "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")"]

print("Welcome to the PyPasswords generator!")
nr_letters = int(input("How many letters in the password?\n"))
nr_numbers = int(input("How many numbers in the password?\n"))
nr_symbols = int(input("How many symbols in the password?\n"))

passw = []
random.seed()

for num in range(0, nr_letters):
    let = random.choice(letters)
    passw.append(let)

for num in range(0, nr_numbers):
    numb = random.choice(numbers)
    passw.append(numb)

for num in range(0, nr_symbols):
    sym = random.choice(symbols)
    passw.append(sym)

random.shuffle(passw)
password = ""
print(password.join(passw))
