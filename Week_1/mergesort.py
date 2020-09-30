import datetime

filename = "data.txt"

##TODO comment out your code

def merge(left,right):
    i = j = 0
    sort = []
    while i<len(left) and j < len(right):
        if left[i] < right [j]:
            sort.append(left[i])
            i += 1
        sort.append(right[j])
        j += 1
    
    sort += left[i:]
    sort += right[j:]
    
    return sort

def mergeSort(array): ##TODO Optimize this below, the above has been changed to reflect my style

    if len(array) >1:

        # Set the middle of the array and split the array into two based on the midpoint (left and right)
        mid = length // 2
        left = mergeSort(array[:mid])
        right = mergeSort(array[mid:])

        return merge(left, right)

# Primary File Handling ##TODO Look at the code below and tweak as needed
with open(filename, "rb") as file:
    for line in file:
        # Strip out the newline character from each line
        newline = line.rstrip('\n')
        # Convert string to an array of unsorted integers
        unsorted = map(int, newline.split(' '))
        # Pass unsorted array to merge sort function (ignoring the first index because we don't need it)
        sorted = mergeSort(unsorted[1:])
        # Convert the result of sorted into a string
        string = ' '.join(str(e) for e in sorted)
        # Write each line to a text file called 'merge.txt'
        with open('merge.txt', 'a') as mergeFile:
            mergeFile.write(string)
            mergeFile.write('\n')
    # Generate a time stamp to the end of the 'merge.txt' file
    with open('merge.txt', 'a') as mergeFile:
        date = datetime.datetime.now()
        mergeFile.write("Executed on: " + str(date))
        mergeFile.write('\n\n')