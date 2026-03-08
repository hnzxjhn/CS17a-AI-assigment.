from itertools import combinations

# Transactions in a small grocery store
transactions = [
    ['milk','bread','butter'],
    ['bread','butter','jam'],
    ['milk','bread'],
    ['milk','butter'],
    ['bread','jam']
]

# Items we want to analyze
items = ['milk','bread','butter','jam']

print("Support for item combinations:")

# Generate combinations of 1 to all items
for i in range(1, len(items)+1):
    for c in combinations(items, i):
        count = 0
        for t in transactions:
            if set(c).issubset(t):
                count += 1
        print(c, "support:", count)