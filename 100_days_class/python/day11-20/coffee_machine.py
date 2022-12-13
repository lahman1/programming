# Creating a coffee machine
# expresso 50 ml water 18g coffee 1.5
# latte 200ml water 24g coffee 150 ml milk 2.5
# cap 250ml water 24g coffee 100 ml milk 3

print("Welcome to Lahman's coffee")
#water = input("starting water?").int()
water = 300
milk = 200
coffee = 100

def make_expresso(exp_water,exp_coffee):
    global water
    global coffee
    water = water - exp_water
    coffee = coffee - exp_coffee

def make_latte(lat_water,lat_coffee,lat_milk):
    global water
    global milk
    global coffee
    water = water - lat_water
    coffee = coffee - lat_coffee
    milk = milk - lat_milk

def make_cap(cap_water,cap_coffee,cap_milk):
    global water
    global milk
    global coffee
    water = water - cap_water
    coffee = coffee - cap_coffee
    milk = milk - cap_milk

what_make_input = input("What kind of coffee would you like?\nPress 1 for an expresso\nPress 2 for a latte\nPress 3 for a cap\n# ")
what_make = int(what_make_input)
if what_make == 1:
    make_expresso(50,18)
elif what_make == 2:
    make_latte(200,24,150)
elif what_make == 3:
    make_cap(250,24,100)
print(water)
print(coffee)
