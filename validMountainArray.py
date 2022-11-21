""" valid mountain array"""
#
def valid_mountain_array(arr):
    """ valid mountain array """
    if len(arr) < 3: # if the array is less than 3, it is not a mountain
        return False
    i = 1 # start at the second element
    while (i < len(arr) and arr[i] > arr[i - 1]): # while the element is greater than the previous element
        i += 1
        if (i == 0 or i == len(arr)): # if the element is the first or last element, it is not a mountain
            return False
    while( i < len(arr) and arr[i] < arr[i - 1]): # while the element is less than the previous element
        i += 1
    return i == len(arr)

# print(valid_mountain_array([2, 1]))
# print(valid_mountain_array([3, 5, 5]))
# print(valid_mountain_array([0, 3, 2, 1]))
print(valid_mountain_array([0, 2, 3, 4, 5, 2, 1, 0]))
