#4
from itertools import permutations

def pies(n):
    letters = [chr(ord('a') + i) for i in range(n)]
    result = [''.join(p) for p in permutations(letters)]
    return sorted(result)

n = 3
lista = pies(n)
for k in lista:
    print(k)