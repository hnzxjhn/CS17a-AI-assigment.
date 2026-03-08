from itertools import combinations

# Transactions in an electronics store
transactions = [
    ['laptop','mouse','keyboard'],
    ['laptop','mouse'],
    ['mouse','keyboard'],
    ['laptop','keyboard'],
    ['laptop','mouse','keyboard','headset']
]

# Items to analyze
items = ['laptop','mouse','keyboard','headset']

print("Support for item combinations:")

for i in range(1, len(items)+1):
    for c in combinations(items, i):
        count = 0
        for t in transactions:
            if set(c).issubset(t):
                count += 1
        print(c, "support:", count)