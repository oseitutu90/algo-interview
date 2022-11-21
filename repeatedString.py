"""There is a string,s, of lowercase English letters that is repeated infinitely many times. 
Given an integer,n, find and print the number of letter a's in the first  letters of the infinite string."""
# print(repeatedString(aba,10)==7)
def repeatedString(s, n):
    """Find and print the number of letter a's in the first n letters of the infinite string."""
    if len(s) == 1 and s == 'a':
        return n
    else:
        return s.count('a')*(n//len(s)) + s[:n%len(s)].count('a')
    
s = 'aba'
n = 10
s2='b'
n2= 12
print(repeatedString(s,n))
print(repeatedString(s2,n2))
