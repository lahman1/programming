# day 3.1

print("Welcome to the Love Calculator")
name1 = input("What is your name?\n")
name2 = input("What is thier name?\n")

low_comb = name1.lower() + name2.lower()
ct = (low_comb.count("t"))
cr = (low_comb.count("r"))
cu = (low_comb.count("u"))
ce = (low_comb.count("e"))
cl = (low_comb.count("l"))
co = (low_comb.count("o"))
cv = (low_comb.count("v"))
ce = (low_comb.count("e"))

num1 = str(ct + cr + cu + ce)
num2 = str(cl + co + cv + ce)
tot = (num1 + num2)
total = int(tot)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
