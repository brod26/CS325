# Bryan Rodriguez-Andrade
# CS 325 Fall 2020
# HW-1 insertTime

import time
import random

# Python code for implementation of MergeSort pulled from https://www.geeksforgeeks.org/merge-sort/


def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# File handling
with open("data.txt", "r") as infile:  
    for line in infile:
        new_array = (line.strip().split())  #loops through every line in the file and creates a new array
        array_to_sort = [int(i) for i in new_array]  #creates a new comprehension of the stripped and split array
        insertionSort(array_to_sort)  #passes the array to the sort
        with open('insert.out.txt', "a") as outfile:  #writes the newly written array to the outfile
            outfile.write(' '.join(str(i) for i in array_to_sort))
            outfile.write('\n')


# Ranges to be used in the random array
n=[5000, 10000, 15000, 20000, 30000, 40000, 50000]

# Run Merge Sort and collect the running time on the program
counter=0
while counter < len(n):
    start=time.time()
    insertionSort([random.randint(0, 10000) for i in range(n[counter])])
    stop=time.time()
    print("Sorts Executed " + str(counter + 1),"Run time: " + str(stop - start))
    counter += 1
