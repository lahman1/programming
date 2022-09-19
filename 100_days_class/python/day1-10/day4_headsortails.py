import random

h_t = random.randint(0, 1)

if h_t == 0:
    print("Heads")
elif h_t == 1:
    print("Tails")
else:
    print("Error: Unknown")
