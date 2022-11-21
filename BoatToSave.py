"""Find the number of boats to save people."""

from array import array


def numRescueBoats(people, limit):
    """Find the number of boats to save people."""
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1
    return boats



# print(numRescueBoats([1, 2], 3))
print(numRescueBoats([3,2,1,3], 4))