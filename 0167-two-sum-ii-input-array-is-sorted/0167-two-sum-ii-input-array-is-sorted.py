class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return aug17_25(numbers, target)

def aug17_25(nums, target):
    '''TC = n, SC = n'''

    i , j = 0, len(nums)-1

    while i < j:
        
        x, y = nums[i], nums[j]

        total = x+y

        if total == target:
            return [i+1, j+1]
        elif total > target:
            j -= 1
        elif total < target:
            i += 1
    
    return [-1, -1]


    
def ans(nums, target):
    '''TC=n, SC=1'''
    N = len(nums)
    i, j = 0, N-1
    
    while i < j:
        
        total = nums[i] + nums[j]
        
        if total == target:
            return [i+1, j+1]
        elif total > target:
            j -= 1
        elif total < target:
            i += 1
    
    return [0, 0]

'''
[2,7,11,15]
9
[2,3,4]
6
[-1,0]
-1
'''