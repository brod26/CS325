import time
import random

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Primary File Handling ##TODO Look at the code below and tweak as needed
with open("data.txt", "r") as infile:
    for line in infile:
        new_array = (line.strip().split())
        array_to_sort = [int(i) for i in new_array]
        mergeSort(array_to_sort)
        with open('merge.out.txt', "a") as outfile:
            outfile.write(' '.join(str(i) for i in array_to_sort))
            outfile.write('\n')


# Ranges to be used in the random array
n = [5000,10000,15000,20000,30000,40000,50000]

# Run Merge Sort and collect the running time on the program
counter = 0
while counter < len(n):
    start = time.time()
    mergeSort([random.randint(0,10000) for i in range(n[counter])])
    stop = time.time()
    print("Sorts executed: " + str(counter + 1), "Run time: " + str(stop - start))
    counter +=1