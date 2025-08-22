from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return aug21_25(ransomNote, magazine)
    
    def ans_2(self, ransomNote: str, magazine: str) -> bool:
        
        if len(magazine) < len(ransomNote):     # Edge case scenario which can optimize the code
            return False
        
        dict = Counter(magazine)            # TC = O(m)
        print(len(dict))
        
        for i in ransomNote:
            
            if i not in dict:
                return False
            
            if dict[i] <=0:
                return False
            
            dict[i] -= 1
            
        return True
    
    
    def ans_1(self, ransomNote: str, magazine: str) -> bool:
        # TC = O(n+m)
        # SC = O(m)
        dict = Counter(magazine)            # TC = O(m)
        print(dict)
        
        for i in ransomNote:
            if i in dict:
                if dict[i] > 0:
                    dict[i] -= 1
                else:
                    return False
            else:
                return False
            
        return True


def aug21_25(ransomNote, magazine):
    '''TC = n, SC = 26 = 1'''

    if len(ransomNote) > len(magazine):         #optimization
        return False

    d = {}

    for c in magazine:
        d[c] = d.get(c, 0) + 1

    for c in ransomNote:
        if c in d and d[c] > 0:
            d[c] -= 1
        else:
            return False
    
    return True

    
