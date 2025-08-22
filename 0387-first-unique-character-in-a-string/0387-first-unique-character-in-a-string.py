class Solution:
    def firstUniqChar(self, s: str) -> int:
        return aug21_25(s)

def aug21_25(s):
    '''TC = n, SC = n'''
    d = {}

    for i, c in enumerate(s):
        
        if c not in d:
            d[c] = [i, 1]
        else:
            temp = d[c]
            temp[1] += 1
            d[c] = temp

    for k, v in d.items():
        if v[1] == 1:
            return v[0]

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
