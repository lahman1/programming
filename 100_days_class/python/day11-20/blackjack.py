# Welcome to python blackjack
import random

cards = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10, "king": 10, "ace": 11}
names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]

dealer_card1 = random.choice(names)
user_card1 = random.choice(names)
dealer_card2 = random.choice(names)
user_card2 = random.choice(names)

print(f"Your first card is a {user_card1}, second card is a {user_card2}")
print(f"Dealer is showing a {dealer_card2}")
user_total = (cards[user_card1] + cards[user_card2])
print(f"Your current total is {user_total}")
dealer_total = (cards[dealer_card2])
print(f"Dealers total is {dealer_total}")

hit = input("Would you like to hit? (yes/no)\n# ").lower()
while hit == "yes":
    new_card1 = random.choice(names)
    print(f"Your new card is a {new_card1}")
    user_total = user_total + cards[new_card1]
    print(f"Your new total is {user_total}")
    if user_total < 22:
        hit = input("Would you like to hit? (yes/no)\n# ").lower()
    elif user_total > 21:
        print("YOU LOST")
        exit()
else:
    exit()
