'''
"anagram"
"nagaram"
"rat"
"car"
'''
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return aug21_25(s, t)

def aug21_25(s, t):
    '''TC = n, SC = 26 = 1'''

    if len(s) != len(t):
        return False

    d = {}

    for c in s:
        d[c] = d.get(c, 0) + 1
    
    for c in t:
        if c in d and d[c] > 0:
            d[c] -= 1
        else:
            return False
    
    return True

 
def dec18(s, t):
    
    if len(s) != len(t):
        return False
    
    d = {}
    
    for c in s:
        d[c] = d.get(c, 0) + 1
    
    for c in t:
        d[c] = d.get(c, 0) - 1
        
    for k,v in d.items():
        if v != 0:
            return False
        
    return True
    
'''I like this'''
def dec17(s, t):
    
    if len(s) != len(t):
        return False
    
    d = {}
    
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
            
    for c in t:
        if c in d and d[c] > 0:
            d[c] -= 1
        else:
            return False
    
    return True
    
    
    


def old1(self, s: str, t: str) -> bool:
    ''' TC = n, SC = n+m '''

    if len(s) != len(t):
        return False

    d = {}

    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for c in t:
        if c in d and d[c] > 0:
            d[c] -= 1
        else:
            return False

    return True

def old2(self, s: str, t: str) -> bool:
    source = Counter(s)
    target = Counter(t)
    print(source)
    print(target)
    return True if source == target else False


'''TC = n, SC = 1, My first attempt'''                
def oct11(s, t):
    
    if len(s) != len(t):
        return False
    
    a = [0] * 26
    
    for c in s:
        idx = ord(c) - ord('a')
        a[idx] += 1
    
    for c in t:
        idx = ord(c) - ord('a')
        a[idx] -= 1
        
    for n in a:
        if n != 0:
            return False
    return True


def oct12(s, t):
    
    if len(s) != len(t):
        return False
    
    a = [0]*26
    
    for i in range(len(s)):
        sc = s[i]
        tc = t[i]
        idxs = ord(sc) - ord('a')
        idxt = ord(tc) - ord('a')
        
        a[idxs] += 1
        a[idxt] -= 1
    
    for n in a:
        if n != 0:
            return False
    return True

def oct12_best(s, t):
    
    if len(s) != len(t):
        return False
    
    d = {}
    
    for i in range(len(s)):
        sc = s[i]
        tc = t[i]
        
        d[sc] = d.get(sc, 0) + 1
        d[tc] = d.get(tc, 0) - 1
    
    for k, v in d.items():
        
        if v != 0:
            return False
    return True
            
    
