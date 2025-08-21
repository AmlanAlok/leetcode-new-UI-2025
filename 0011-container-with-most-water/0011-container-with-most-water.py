class Solution:
    def maxArea(self, height: List[int]) -> int:
        return aug21_25(height)


def aug21_25(height):
    '''TC = n, SC = 1'''
    
    N = len(height)
    i, j = 0, N-1

    _max = 0

    while i < j:
        l, r = height[i], height[j]

        breadth = j-i
        h = min(l, r)

        _max = max(_max, h * breadth)

        if l < r:
            i += 1
        else:
            j -= 1
    
    return _max




def ans(nums):
    
    N = len(nums)
    
    i, j = 0, N-1
    max_vol = 0
    
    while i < j:
        
        base = j-i
        height = min(nums[i], nums[j])
        
        vol = base * height
        
        max_vol = max(vol, max_vol)
        
        if nums[i] < nums[j]:
            temp = nums[i]
            while nums[i] <= temp and i < j:
                i += 1
        else:
            temp = nums[j]
            while nums[j] <= temp and i < j:
                j -= 1
    
    return max_vol

'''
[1,8,6,2,5,4,8,3,7]
[1,1]
'''
    
def ans1(height: List[int]) -> int:

    i, j = 0, len(height)-1
    maxv = -1

    while i<j:
        # print(i, j)
        w = j-i
        h = min(height[i], height[j])

        area = w*h

        if area > maxv:
            maxv = area

        if height[i] < height[j]:
            temp = height[i]
            while height[i] <= temp and i<j:
                i += 1
        else:
            temp = height[j]
            while height[j] <= temp and i<j:
                j -= 1

    return maxv