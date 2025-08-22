class Solution:
    def firstUniqChar(self, s: str) -> int:
        return aug21_25(s)

def aug21_25(s):
    '''TC = n, SC = 26 = 1'''
    
    d = {}

    for i, c in enumerate(s):
        d[c] = d.get(c, 0) + 1

    for i, c in enumerate(s):
        if d[c] == 1:
            return i

    return -1


    
def ans(s):
    '''Tc=n, SC=26=1'''
    count = collections.Counter(s)

    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx     
    return -1

'''
"leetcode"
"loveleetcode"
"aabb"
"dddccdbba"
'''
