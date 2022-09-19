# Program to operate a blind auction.

bids = {}
amounts = []

print("Welcome to the auction")
run = True

while run:
    name = input("Please enter your name? ")
    bid = int(input("Please enter your bid? $"))
    more = input("Are there more bids? (yes/no): ").lower()
    if more == "no":
        run = False
    bids[bid] = name
    for bid in bids:
        amounts.append(bid)

high_bid = max(amounts)
high_name = bids[high_bid]

winner = (f"Winner is {high_name} with a bid of ${high_bid}")
print(winner)
