# Bryan Rodriguez-Andrade
# CS 325 Fall 2020
# HW-1 insertionsort

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
        # loops through every line in the file and creates a new array
        new_array = (line.strip().split())
        # creates a new comprehension of the stripped and split array
        array_to_sort = [int(i) for i in new_array]
        insertionSort(array_to_sort)  # passes the array to the sort
        # writes the newly written array to the outfile
        with open('insertion.out.txt', "a") as outfile:
            outfile.write(' '.join(str(i) for i in array_to_sort))
            outfile.write('\n')
