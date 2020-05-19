#!/usr/local/bin/python

import math
from io import StringIO
import random
from time import time
import funs

def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    # show_tree(arr)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)

def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write(u'\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(u'%s' % (str(n).center(col_width, fill)))
        last_row = row
    print ('-' * total_width)
    print (output.getvalue())
    print ('-' * total_width)
    return

if __name__ == "__main__":
    LEN = int(1e5)
    print 'generating data...'
    data = [random.randint(0, LEN) for _ in range(LEN)]
    print 'sorting...'
    start = time()
    heapSort(data)
    print 'complete with time cost: ' + str(time() - start) + " seconds."
    print 'verifying...' + str(funs.check(data))