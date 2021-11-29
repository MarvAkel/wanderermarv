import random

possible = [(0,1),(2,3)]
x = (1,2)
possible.append(tuple(x))
print(possible)
print(random.choice(possible))

