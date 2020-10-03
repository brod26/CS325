# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 

# Primary File Handling ##TODO Look at the code below and tweak as needed
with open("data.txt", "r") as infile:
    for line in infile:
        new_array = (line.strip().split())
        array_to_sort = [int(i) for i in new_array]
        insertionSort(array_to_sort)
        with open('insertion.out.txt', "a") as outfile:
            outfile.write(' '.join(str(i) for i in array_to_sort))
            outfile.write('\n')