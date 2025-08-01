from collections import deque

class Solution:
    def removeDuplicates(self, s: str) -> str:
        return aug01_25(s)

def aug01_25(s):
    '''TC = n, SC = n'''
    stack = deque()

    for c in s:
        if stack:
            if stack[-1] == c:
                stack.pop()
                continue
        stack.append(c)

    return ''.join(stack)

'''
"abbaca"
"azxxzy"
'''
