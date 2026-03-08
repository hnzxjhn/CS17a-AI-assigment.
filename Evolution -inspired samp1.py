import random

gene = "101010"

def mutate(g):
    pos = random.randint(0,len(g)-1)
    g = list(g)
    g[pos] = '1' if g[pos]=='0' else '0'
    return "".join(g)

print("Original:",gene)
print("Mutated:",mutate(gene))