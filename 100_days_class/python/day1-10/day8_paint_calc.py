
import math


def paint_calc(height, width, cover):
    amount = (test_h * test_w) / coverage
    rod = (math.ceil(amount))
    print(f"You'll need {rod} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
