
numbers = (list(range(1, 101)))
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

total = sum(evens)
print(total)
