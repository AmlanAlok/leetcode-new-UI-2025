class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return aug29_25(nums, target)

def aug29_25(nums, target):
    '''TC = n log(n) + n^3, SC = n for sorting'''

    N = len(nums)

    if N < 4:
        return []

    nums.sort()

    ans = []
    last_a = None

    for a in range(N-3):

        if last_a == nums[a]:
            continue

        last_b = None

        for b in range(a+1, N-2):
            
            if nums[b] == last_b:
                continue

            c, d = b+1, N-1

            while c < d:

                n1, n2, n3, n4 =  nums[a], nums[b], nums[c], nums[d]

                _sum = n1 + n2 + n3 + n4

                if _sum == target:

                    # if a != b != c != d:
                    ans.append([n1, n2, n3, n4])
                    c += 1
                    d -= 1

                    while c < d and nums[c] == n3:
                        c += 1
                
                elif _sum < target:
                    while c < d and nums[c] == n3:
                        c += 1
                
                elif _sum > target:
                    while c < d and nums[d] == n4:
                        d -= 1
                
                last_b = n2
        
        last_a = n1
    
    return ans

'''
[2,2,2,2,2]
8
[1,0,-1,0,-2,2]
0
[1,0]
0
'''
