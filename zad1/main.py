#1[10, 22, 9, 33, 21, 50, 41, 60, 80]

def kurczak(numbers):
    if not numbers:
        return []
    n = len(numbers)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(1, n):
        best_j = max(
            filter(lambda j: numbers[j] < numbers[i], range(i)),
            key=lambda j: dp[j],
            default=None
        )
        if best_j is not None:
            dp[i] = dp[best_j] + 1
            prev[i] = best_j