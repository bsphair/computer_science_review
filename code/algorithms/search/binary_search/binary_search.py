averages = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search_interative(data, num):
    low = data[0]
    high = data[len(data) - 1]
    
    while low <= high:
        mid = (high + low) // 2
        if num == mid:
            return mid
        elif num > mid:
            low = mid + 1
        else:
            high = mid - 1
    
    return 'Number does not exist'
    
    
def binary_search_recursive(data, low, high, num):
    if low <= high:
        mid = (high + low) // 2
        if num == mid:
            return 'found'
        elif num > mid:
            return binary_search_recursive(data, mid + 1, high, num)
        elif num < mid:
            return binary_search_recursive(data, low, mid - 1, num)
    else:
        return 'Number does not exist'

print(binary_search_interative(averages, 1))
print(binary_search_recursive(averages, 0, len(averages) - 0, 1))

