#!/usr/local/bin/python

def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    for gap in range(10, -1, -1):
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp


data = [9, 8, 2, 1, 3, 6, 7, 2, 3, 1, 7, 3, 7, 5, 6, 4, 1]
size = len(data)
shellSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)