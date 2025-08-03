from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return aug01_25(s)

def aug02_25(s):

    s = '012345'
    c = 0
    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            print(s[i:j], '     ', (i, j))
            c += 1
    
    print('---')
    print(c)

    return 0

def aug01_25(s):

    stack = deque()
    stack.append(-1)
    maxlen = 0

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            last_idx = stack.pop()

            if len(stack) == 0:
                stack.append(i)
            else:
                sublen = i - stack[-1]
                maxlen = max(maxlen, sublen)

    return maxlen


            

            

