class Solution:
    def frequencySort(self, s: str) -> str:
        return aug21_25(s)

def aug21_25(s):
    '''TC = n + k log(k), SC = n, where n = length of input string and k = no. of unique char in the string'''
    '''TC = n log(n) if input has all unique chars'''
    
    d = {}

    for c in s:
        d[c] = d.get(c, 0) + 1
    
    sorted_d = dict(sorted(d.items(), key = lambda x: x[1], reverse = True))        # TC = k log(k)

    res = []            # SC = n

    for k, v in sorted_d.items():
        for _ in range(v):
            res.append(k)
    
    return ''.join(res)
        