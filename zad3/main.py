#3

def chomik(n):
    if n <= 0:
        return []

    def dfs(remaining, start):
        if remaining == 0:
            return [[]]
        sequences = []
        for i in range(start, remaining + 1):
            for seq in dfs(remaining - i, i):
                sequences.append([i] + seq)
        return sequences

    return dfs(n, 1)


n = 5
result = chomik(fn)
print(f"{n}")
for seq in result:
    print(seq)
#1