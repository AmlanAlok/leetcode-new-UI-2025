from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        return jul31_25(s)
    
    def ans1(self, s: str) -> bool:
        
        a=deque()
        
        for v in s:
            
            if a:
                if v==')' and a[-1] == '(' or v=='}' and a[-1]=='{' or v == ']' and a[-1]=='[':
                    a.pop()
                    continue
            
            a.append(v)
            
        return len(a)==0
    
    def p1(self, s: str) -> bool:
        
        a = []
        
        for i in s:
            
            if a:
                if (i == '}' and a[-1] == '{') or (i == ')' and a[-1] == '(') or (i == ']' and a[-1] == '['):
                    a.pop()
                    continue
            
            a.append(i)
        
        return len(a)==0

    def p2(self, s: str) -> bool:
        
        a = []
        
        for i in range(len(s)):

            x = s[i]
            
            if a:
                if (x==')' and a[-1]=='(') or (x=='}' and a[-1]=='{') or (x==']' and a[-1]=='['): 
                    a.pop()
                    continue
                
            a.append(x)
            
        return len(a)==0
            
def oct22(s):
    st = deque()
    
    for c in s:
        
        if st:
            
            x = c == ')' and st[-1] == '('
            y = c == '}' and st[-1] == '{'
            z = c == ']' and st[-1] == '['
            
            if x or y or z:
                st.pop()
                continue
        
        st.append(c)
    
    return len(st) == 0

def dec02(s):
    
    st = deque()
    
    for c in s:
        
        if st:
            if (c == ')' and st[-1] == '(') \
            or (c == '}' and st[-1] =='{') \
            or (c == ']' and st[-1] == '['):
                st.pop()
                continue
            
        st.append(c)
    
    return len(st) == 0

def dec27(s):
    
    stack = deque()
    
    for c in s:
        
        if stack:
            b1 = c == ')' and stack[-1] == '('
            b2 = c == '}' and stack[-1] == '{'
            b3 = c == ']' and stack[-1] == '['
            
            if b1 or b2 or b3:
                stack.pop()
                continue
        
        stack.append(c)
    
    return len(stack) == 0

def jul31_25(s):

    stack = deque()

    for c in s:
        if stack:
            if (stack[-1] == '(' and c == ')') or (stack[-1] == '[' and c == ']') or (stack[-1] == '{' and c == '}'):
                stack.pop()
                continue
        stack.append(c)

    return len(stack) == 0


'''
"()"
"()[]{}"
"(]"
"([])"
"([)]"
'''