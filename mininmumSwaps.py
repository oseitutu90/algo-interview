"""You are given an unordered array consisting of consecutive integers 
[1, 2, 3, ..., n] without any duplicates. 
You are allowed to swap any two elements. Find 
the minimum number of swaps required to sort the array in ascending order."""

def minimumSwaps(arr):
    """minimum swaps to sort array in ascemding order"""
    swap = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
            swap += 1
    return swap
        

print(minimumSwaps([7, 1, 3, 2, 4, 5, 6])==5)
print(minimumSwaps([2, 3, 4, 1, 5,])==3)