averages = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def findNum(data, num):
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
    


pos = findNum(averages, 1)
print(pos)
