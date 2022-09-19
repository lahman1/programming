# Creating game to see who pays for the bill
import random

# using a set list
# players = ["Andrew", "Karen", "Kelly", "Kheylani", "Archer"]

# creating a list from input
players = input("Which players would you like to play?\n")
players = players.split(", ")


lenth = len(players)
pay_up = random.randint(0, lenth - 1)
who_pays = players[pay_up]
print(f"{who_pays} is paying")
