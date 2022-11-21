def findDuplicate(string):
    """Find  consecutive duplicate letters in a string."""
    hash_set = set()
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            hash_set.add(string[i])
    return hash_set if hash_set else None
    
string = "Helloo World"
print(findDuplicate(string))
