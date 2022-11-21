"""Two numbers which sum to a target value."""

def targetSum(numbers, target):
    """Find two numbers which sum to a target value."""
    hash_set = set()
    for i,number in enumerate(numbers):
        if target - number in hash_set: 
            return [i, numbers.index(target - number)]
            #else add it to the hash set
        hash_set.add(number)
    return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(targetSum(numbers, 10))