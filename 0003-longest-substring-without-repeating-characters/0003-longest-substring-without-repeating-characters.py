class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return aug31_25(s)

def aug31_25(s):

    d = {}
    i = j = 0
    _max = 0
    N = len(s)

    while j < N:

        c = s[j]
    
        if c in d:
            i = max(i, d[c]+1)  # important, I should be the char after the previous occurence
        
        d[c] = j
        _max = max(_max, j-i+1)

        j += 1

    return _max


def jan1(s):
    
    l = len(s)
    last_idx = {}
    maxi = 0
    i = 0
    
    for j in range(l):
        c = s[j]
        
        if c in last_idx and last_idx[c]+1 > i:
            i = last_idx[c]+1
        
        last_idx[c] = j
        maxi = max(maxi, j-i+1)
        
    return maxi
            
def dec31(s):
    
    maxi = 0
    l = len(s)
    d = {}
    i = 0
    
    for j in range(l):
        
        c = s[j]
        
        if c in d:
            i = max(d[c]+1, i)
        
        maxi = max(maxi, j-i+1)
        d[c] = j
    
    return maxi    

def old1(self, s: str) -> int:
    m = 0
    q = 0
    d = {}
    a = []

    for i in range(len(s)):
        c = s[i]

        if c in d:
            pass
        else:
            a.append(c)

def ans1(s):
    '''
    TC = n
    SC = O(min(m, n))  = We need O(k). k is the size of dict or set.
    n is the length of string. worst case when all chars are unique.
    m are the num of chars in the alphabet.
    '''
    i = j = 0
    d = {}
    ans = 0
    
    while j < len(s):
        c = s[j]
        
        if c not in d:
            d[c] = j
        else:
            i = max(d[c] + 1, i)    # so that i does not go back to an old index 0 "abba"
            d[c] = j        # updating index with latest occurrence
        
        ans = max(ans, j-i+1)
        
        j += 1
    
    return ans

def ans2(s):
    i = j = 0
    d = {}
    ans = 0
    
    while j <len(s):
        c = s[j]
        
        if c in d and d[c] >= i:
            i = d[c] + 1
        else:
            ans = max(ans, j-i+1)
        
        d[c] = j
        j += 1
    
    return ans
        
def dec20(s):
    
    i = j = 0
    d = {}
    mx = 0
    
    for j in range(len(s)):
        
        c = s[j]
        
        if c not in d:
            d[c] = j
        else:
            i = max(d[c]+1, i)
            d[c] = j
            
        mx = max(mx, j-i+1) # this +1 helped to resolve " " case
        '''
        It corrects the +1 added earlier to i
        If all chars are unique, the +1 gives the length with 0-indexed arrays
        '''
        
    return mx

def dec22(s):
    
    i = j = 0
    d = {}
    mx = 0
    
    for j in range(len(s)):
        c = s[j]
        
        if c in d:
            i = max(d[c]+1, i)
        d[c] = j
            
        mx = max(mx, j-i+1) # this +1 helped to resolve " " case
        '''
        It corrects the +1 added earlier to i
        If all chars are unique, the +1 gives the length with 0-indexed arrays
        
        The current value of i is where the last duplication occurred. So any new valid string will have to start after it.
        '''
        
    return mx

def x(s):
    
    d = {}
    l = len(s)
    i = 0
    mx = 0
    
    for j in range(l):
        c = s[j]
        
        if c in d:
            i = max(d[c]+1, i)
        
        mx = max(mx, j-i+1)
        d[c] = j
    
    return mx
            
def p(s):
    
    d = {}
    n = len(s)
    i = 0
    mx = 0
    
    for j in range(n):
        c = s[j]
        
        if c in d:
            i = max(i, d[c] + 1)
        d[c] = j
        
        mx = max(mx, j-i+1)
    
    return mx
        
def prac(s):

	max_len = 0
	dict = {}
	i = j = 0
	n = len(s)

	while j < n:

		c = s[j]

		if c in dict:
			i = max(dict[c] + 1, i)
		
		dict[c] = j
		max_len = max(max_len, j-i+1)

		j += 1

	return max_len

def prac2(s):
    maxlen = 0
    N = len(s)
    i = j = 0
    d = {}
    
    while j < N:
        c = s[j]
        
        if c in d:
            i = max(d[c]+1, i)
        
        d[c] = j
        maxlen = max(maxlen, j-i+1)
        
        j += 1
    
    return maxlen
        

'''
"abcabcbb"
"bbbbb"
"pwwkew"
"abba"
"abcdeafbdgcbb"
" "
'''