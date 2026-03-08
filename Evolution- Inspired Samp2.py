import random

population = [random.randint(0,31) for _ in range(6)]

def fitness(x):
    return x*x

for generation in range(5):
    population = sorted(population, key=fitness, reverse=True)
    population = population[:3] + [random.randint(0,31) for _ in range(3)]
    print("Generation",generation,population)