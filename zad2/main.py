#2[2, -4, 6, 8, -10, 100, -6, 5]

def kot(numbers):
    
    if not numbers:
        return []
    
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    current_start = 0
    max_length = 0
    
    for i, num in enumerate(numbers):
        current_sum += num
