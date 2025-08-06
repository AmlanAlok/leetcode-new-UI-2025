from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return aug03_25(nums)

def aug03_25(nums):
    '''TC = n, SC = n'''

    stack = deque()
    N = len(nums)
    ans = [-1] * N

    for k in range(N*2-1, -1, -1):        # important cirlular looping

        i = k % N

        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()

        if stack:
            ans[i] = nums[stack[-1]]

        stack.append(i)

    return ans

'''
[1,2,1]
[1,2,3,4,3]
[5,4,3,2,1]
[2,2,2]
'''





        