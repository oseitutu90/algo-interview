
""""takes in two strings and returns the index of the first 
occurence of the first string in the second string"""

def two_string(string1, string2):
    """Find the index of the first occurence of the first string in the second string."""
    if len(string2) >= len(string1) and string1 in string2:
        string1 = string1.lower()
        string2 = string2.lower() # convert both strings to lowercase
        return string2.index(string1) # return the index of the first occurence of the first string in the second string
    else:
        return -1 


string2 = "Hello the world is not as blue as you think"
string1 = "world"
print(two_string(string1, string2))
