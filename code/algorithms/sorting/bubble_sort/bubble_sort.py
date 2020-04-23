averages = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def bubble_sort(data):
    dataLenth = len(data)
    for a in range(dataLenth):
        for b in range(0, dataLenth - 1):
            if data[b] > data[b + 1]:
                temp = data[b]
                data[b] = data[b + 1]
                data[b + 1] = temp


bubble_sort(averages)
print(averages)
