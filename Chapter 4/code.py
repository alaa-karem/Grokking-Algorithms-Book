# Quick-Sort code:
def quickSort(array):
    if len(array)<2:                    # base-case
        return array
    else:
        pivot = array[0]               # Recursive case
        less = [i for i in array[1:] if i <= pivot]   #Sub-array of all the elements less than the pivot
        greater = [i for i in array[1:] if i > pivot] #Sub-array of all the elements greater than the pivot
        return quickSort(less) + [pivot] + quickSort(greater)
print( quickSort([10, 5, 2, 3]) )