# Binary-Search code:
def binary_search(list, item):
    low = 0 
    high = len(list)-1 
    while low <= high: 
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item: 
            high = mid - 1
        else: 
            low = mid + 1
    return -1

list = [3,5,10,17,35,50,74,79,120,138,200]
result = binary_search(list,35)
if result !=-1 :
    print("Number you search about is found and its position is: ",str(result))
else:
    print("Sorry!! Number you search about not found")
