class Solution:
    def firstUniqChar(self, s: str) -> int:
        return ans(s)
    
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
