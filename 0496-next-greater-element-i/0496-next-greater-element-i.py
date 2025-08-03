from collections import deque

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return aug03_25(nums1, nums2)

def aug03_25(nums1, nums2):
    '''TC = n, SC = n'''
    stack = deque()         #n
    next_greater = {}       #n
    ans = []

    for n in nums2:

        while stack and stack[-1] < n:
            last = stack.pop()
            next_greater[last] = n
        else:
            stack.append(n)
    
    while stack:
        num = stack.pop()
        next_greater[num] = -1

    for n in nums1:
        next_val = next_greater[n]
        ans.append(next_val)
    
    return ans



