# Bryan Rodriguez-Andrade
# CS 325 Fall 2020
# HW-2 stoogeTime

import time
import random

# Stoogesort code base pulled from geeks for geeks https://www.geeksforgeeks.org/stooge-sort/


def stoogesort(arr, l, h):

    if l >= h:
        return

    # If first element is smaller
    # than last, swap them
    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t

    # If there are more than 2 elements in
    # the array
    if h-l + 1 > 2:
        t = (int)((h-l + 1)/3)

        # Recursively sort first 2 / 3 elements
        stoogesort(arr, l, (h-t))

        # Recursively sort last 2 / 3 elements
        stoogesort(arr, l + t, (h))

        # Recursively sort first 2 / 3 elements
        # again to confirm
        stoogesort(arr, l, (h-t))


# Ranges to be used in the random array
n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Run Stooge Sort and collect the running time on the program
counter = 0
while counter < len(n):

    arr = [random.randint(0, 10000) for i in range(n[counter])]
    size = len(arr) - 1
    start = time.time()
    stoogesort(arr, 0, size)
    stop = time.time()
    print("Sort size " + str(n[counter]), "Run time: " + str(stop - start))
    counter += 1
