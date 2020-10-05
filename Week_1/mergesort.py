# Bryan Rodriguez-Andrade
# CS 325 Fall 2020
# HW-1 Mergesort

# Python code for implementation of MergeSort pulled from https://www.geeksforgeeks.org/merge-sort/
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

# File handling
with open("data.txt", "r") as infile:  
    for line in infile:
        new_array = (line.strip().split())  #loops through every line in the file and creates a new array
        array_to_sort = [int(i) for i in new_array]  #creates a new comprehension of the stripped and split array
        mergeSort(array_to_sort)  #passes the array to the sort
        with open('merge.out.txt', "a") as outfile:  #writes the newly written array to the outfile
            outfile.write(' '.join(str(i) for i in array_to_sort))
            outfile.write('\n')



