class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return aug18_25(s)

def aug18_25(s):
    '''TC = n, SC = 1'''
    
    N = len(s)
    i, j = 0, N-1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    
    return s

    
def ans(s):
    '''TC=n, SC=1'''
    N = len(s)
    i, j = 0, N-1
    
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
        
def ans2(s):
    '''TC=n, SC=1'''
    return s.reverse()

def ans3(s):
    '''TC=n, SC=n'''
    N = len(s)-1
    
    def helper(l, r):
        if l < r:
            s[l], s[r] = s[r], s[i]
            helper(i+1, r-1)
            
    helper(0, N-1)

'''
["h","e","l","l","o"]
["H","a","n","n","a","h"]
["a"]
'''