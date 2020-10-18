# Bryan Rodriguez-Andrade
# CS 325 Fall 2020
# HW-1 stoogeSort

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


# File handling
with open("data.txt", "r") as infile:
    for line in infile:
        # loops through every line in the file and creates a new array
        new_array = (line.strip().split())
        # creates a new comprehension of the stripped and split array
        array_to_sort = [int(i) for i in new_array[1:]]
        size = len(array_to_sort) - 1
        stoogesort(array_to_sort, 0, size)  # passes the array to the sort
        # writes the newly written array to the outfile
        with open('stooge.out.txt', "a") as outfile:
            outfile.write(' '.join(str(i) for i in array_to_sort))
            outfile.write('\n')
