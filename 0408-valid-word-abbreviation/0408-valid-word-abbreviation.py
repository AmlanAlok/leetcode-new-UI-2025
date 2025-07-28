class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # return ans(word, abbr)
        return ans(word, abbr)


def ans(word, abbr):
    '''TC = n, SC = 1'''

    i, j = 0, 0
    N = len(word)
    M = len(abbr)

    while i < N and j < M:
        if word[i] == abbr[j]:
            i+=1
            j+=1
        else:
            if abbr[j] == '0':
                return False
            elif 'a' <= abbr[j] <= 'z':
                return False
            elif '1' <= abbr[j] <= '9':
                # num_str = ''
                start_idx = j
                
                while j < M and '0' <= abbr[j] <= '9':
                    # num_str += abbr[j]        # TC = O(n) as string is immutable        
                    j+=1
                
                num = int(abbr[start_idx:j])
                i += num

    if i == N and j == M:
        return True
    return False
            

'''
not adjacent
not empty
no leading 0
'''
def ans1(word, abbr):
    '''TC=n, SC=1'''
    def is_number(c):
        return True if 48 <= ord(c) <= 57 else False

    i = 0
    j = 0
    M, N = len(word), len(abbr)
    
    while j < M and i < N:
        
        if word[j] == abbr[i]:
            i += 1
            j += 1
        elif abbr[i] == '0':
            return False
        elif is_number(abbr[i]):
            k = i
            while k < N and is_number(abbr[k]):
                k += 1
                
            num = int(abbr[i:k])
            i = k
            j += num
        else:
            return False
    
    return i == N and j == M

def ans2(word, abbr):
    
    N, M = len(word), len(abbr)
    i, j = 0, 0
    
    while i < N and j < M:
        
        if word[i] != abbr[j]:
            
            mismatch = abbr[j]
            
            if mismatch == '0':
                return False
            if mismatch.isalpha():
                return False
            if mismatch.isnumeric():
                
                num_string = ''
                
                while j < M and abbr[j].isnumeric():
                    num_string += abbr[j]
                    j += 1
                
                num = int(num_string)
                
                i += num
        else:
            i += 1
            j += 1
    
    if i == N and j == M:
        return True
    return False
            

'''
"internationalization"
"i12iz4n"
"apple"
"a2e"
"internationalization"
"i5a11o1"
"substitution"
"s55n"
"substitution"
"s010n"
"substitution"
"s10n"
"substitution"
"sub4u4n"
"substitution"
"12"
"substitution"
"su3ilu2on"
"hi"
"hi1"
'''


def discussion(word, abbr):
    i = j = 0
    m, n = len(word), len(abbr)
    while i < m and j < n:
        if word[i] == abbr[j]:
            i += 1
            j += 1
        elif abbr[j] == "0":
            return False
        elif abbr[j].isnumeric():
            k = j
            while k < n and abbr[k].isnumeric():
                k += 1
            i += int(abbr[j:k])
            j = k
        else:
            return False
    return i == m and j == n
        
def fail(word, abbr):
    
    N = len(word)
    M = len(abbr)
    i = 0
    j = 0
    zero = ord('0')
    
    while i < M and j < N:
        
        if word[j] != abbr[i]:
            
            if abbr[i] == zero:
                return False
            
            exp = 0
            num = 0
            
            while i < M and 49 <= ord(abbr[i]) <= 57:
                val = ord(abbr[i]) - zero
                num = (10**exp * num) + val
                i += 1
                exp += 1
            
            if num == 0:
                return False
            
            j = j + num
            
            if j > N:
                return False
        
        else:
            i, j = i + 1, j + 1
        
    return True
            
            
            
            
            
                
            
    
    
    
    
    
    
    
    
    
    