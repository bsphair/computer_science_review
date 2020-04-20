averages = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def max_sub_array(data):
    current = 0
    maxNumber = 0
    
    for num in averages:
        current = max(num + current, 0)
        maxNumber = max(current, maxNumber) 
    return maxNumber

print(max_sub_array(averages))
