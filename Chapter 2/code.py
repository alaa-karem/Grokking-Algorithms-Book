# Selection-Sort code:
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        return smallest_index

def selection_Sort(arr):
    orderedArray = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        orderedArray.append(arr.pop(smallest))
    return orderedArray

print(selection_Sort([5,3,6,2,10]))

