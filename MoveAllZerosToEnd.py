""" are the numbers in the array sorted? 
    if not, sort the array in ascending order.
    if yes, return the array.
"""

def move_zeros(array):
    """
    Move all zeros to the end of the array.
    """
    zeros = []
    for i in array: 
        if i == 0:
            zeros.append(i)
    for i in zeros:
        array.remove(i)
    array.extend(zeros)
    return array

move_zeros([0, 1, 0, 3, 12])
move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]