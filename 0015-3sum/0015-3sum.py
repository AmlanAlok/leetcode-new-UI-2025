class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return aug21_25(nums)
        return ans(nums)

def aug21_25(nums):
    '''TC = n log(n) + n^2, SC = '''
    nums.sort()
    N = len(nums)
    ans = []
    last = None

    for i in range(N-2):

        if nums[i] == last:
            continue

        j, k = i+1, N-1
        
        while j < k:

            x, y, z = nums[i], nums[j], nums[k]
            _sum = x + y + z

            if _sum == 0:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

            elif _sum < 0:
                prev = nums[j]

                while j < k and nums[j] == prev:
                    j += 1
            
            elif _sum > 0:
                prev = nums[k]

                while j < k and nums[k] == prev:
                    k -= 1
            
        last = nums[i]
    
    return ans






    
def ans(nums):
    '''TC=n2, SC=log(n)'''
    N = len(nums)
    nums.sort()
    ans = []
    prev = None
    
    for i in range(N-2):
        
        if nums[i] == prev:
            continue
        
        j = i+1
        k = N-1
        
        while j < k:
            
            t = nums[i] + nums[j] + nums[k]
            sec, third = nums[j], nums[k]
            
            if t == 0:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                
                while j < k and nums[j] == sec:
                    j += 1
                    
            elif t < 0:
                while j < k and nums[j] == sec:
                    j += 1
            elif t > 0:
                while j < k and nums[k] == third:
                    k -= 1
            
        prev = nums[i]
    
    return ans

'''
[-1,0,1,2,-1,-4]
[0,1,1]
[0,0,0]
[-1,0,1,2,-1,-4,2]
[-4,2,2]
[0,0,0,0]
[-2,0,0,2,2]
'''

        
def ans_TLE(nums):
    '''TC=n2, SC=n, No Optimizations'''
    N = len(nums)
    ans = set()
    
    for i in range(N-2):
        x = nums[i]
        d = {}
        target = -x
        
        for j in range(i+1, N):
            y = nums[j]
            
            z = -y -x
            
            if z in d:
                ans.add(tuple(sorted([x,y,z])))
            else:
                d[y] = j
    
    return list(ans)
          
def jan5(nums):
    
    nums.sort()
    l = len(nums)
    ans = []
    
    last_k_val = None
    
    for k in range(l-2):
        
        first = nums[k]
        
        if first == last_k_val:
            continue
            
        i = k+1
        j = l-1
        
        while i < j:
            sec, third = nums[i], nums[j]

            s = first + sec + third
            
            if s == 0:
                ans.append([first, sec, third])
                
                i+=1
                j-=1
                
                while i < j and nums[i] == sec:
                    i+=1
                
            elif s < 0:
                while i < j and nums[i] == sec:
                    i += 1
            elif s > 0:
                while j > i and nums[j] == third:
                    j -= 1
        
        last_k_val = nums[k]
        
    return ans
        
def dec27(nums):
    '''TC = n2, SC = n (worst case)'''
    
    l = len(nums)
    nums.sort()
    prev_first = None
    ans = []
    
    for k in range(l-2):
        
        first = nums[k]
        
        if first == prev_first:
            continue
        
        i, j = k+1, l-1
        
        while i < j:    
            second, third = nums[i], nums[j]
            
            total = first + second + third
            
            if total < 0:
                i += 1
            elif total > 0:
                j -= 1
            else:
                ans.append([first, second, third])
                
                i += 1
                j -= 1
                
                while i < j and nums[i] == second:
                    i += 1
                
        prev_first = first
    
    return ans

def dec26(nums):
    '''TC = n2, SC = '''
    l = len(nums)
    ans_d = {}
    ans = []
    
    for i in range(l):
        
        j = i + 1
        d = {}
        
        while j < l:
            
            target = -(nums[j] + nums[i])
            
            if target not in d:
                d[nums[j]] = j
            else:
                arr = [nums[i], nums[j], target]
                arr.sort()
                x = tuple(arr)
                if x not in ans_d:
                    ans_d[x] = i
            
            j += 1
    
    for nums in ans_d.keys():
        triplet = list(nums)
        ans.append(triplet)
        
    return ans
                
def ans1(nums: List[int]) -> List[List[int]]:
    '''
    A1 - 2 pointers
    This approach is the fastest as it skips duplicates
    '''
    if len(nums) == 0:
        return []

    nums.sort()
    ans = []
    m = nums[0]-1   # so that there is no match

    for k in range(len(nums)-2):

        if nums[k]==m:      # this helps to skip duplicates
            continue

        i = k+1
        j=len(nums)-1

        mi = nums[i]
        mj = nums[j]

        while i<j:
            # print(nums[k])


            s = nums[i]+nums[j]+nums[k]

            if s<0:
                i+=1
            elif s>0:
                j-=1
            else:
                x = [nums[k],nums[i],nums[j]]

                # if x not in ans:  # this line was adding a lot of TC. removing this lowered time from 4000ms to 700ms
                ans.append(x)

                i+=1
                j-=1

                # this helps to skip duplicates
                while i<j and nums[i]==nums[i-1]:   
                    i+=1                    

        m = nums[k]

    return ans

def fail1(self, nums: List[int]) -> List[List[int]]:
    # print('start')
    if nums is [] or nums is [0]:
        return []

        d={v: i for i,v in enumerate(nums)}

        di = d.items()

        print('a')

    d={}
    a=[]

    for i in range(len(nums)):

        v = nums[i]

        if v in d:
            d[v]+=1               
        else:
            d[v] = 1

    # nums.sort()

    for i in range(len(nums)):

        q = d.copy()
        di = q.items()
        x = nums[i]


        for k, v in di:
            c = x+k
            c = -1*c

            if c in q and q[c]>0 and q[k]>0 and q[x]>0:

                q[c]-=1
                q[k]-=1
                q[x]-=1

                if [x,k,c] not in a and q[c]>=0 and q[k]>=0 and q[x]>=0:

                    ins = True
                    for e in a:
                        if x in e and k in e and c in e:
                            ins = False
                    if ins:
                        a.append([x,k,c])

    return a

def ans2(self, nums: List[int]) -> List[List[int]]:
    '''
    Approach 2 - Using hashmap
    '''
    nums.sort()
    print(nums)
    l = len(nums)
    ans=[]
    k=0

    # for k in range(l):
    while k<l-2:

        i = k+1

        d={}

        while i<l:

            c = -1*nums[k] - nums[i]

            if c in d:
                ans.append([nums[k],c,nums[i]])

                # i+=1

                # if i<l and nums[i]==nums[i-1]:
                #     while i<l and nums[i]==nums[i-1]:
                #         i+=1
                if i<l-1 and nums[i]==nums[i+1]:
                    while i<l-1 and nums[i]==nums[i+1]:
                        i+=1

            else:
                d[nums[i]] = i

            i+=1


            # We cannot do this bcuz [-4,2,2], as i and j can have the same value in ans, we cannot skip repeating values when scanning through the array

            # if i<l and nums[i]==nums[i-1]:
            #     while i<l and nums[i]==nums[i-1]:
            #         i+=1

        k+=1

        if nums[k]==nums[k-1]:
            while k<l-2 and nums[k]==nums[k-1]:
                k+=1

    return ans

def ans3(self, nums: List[int]) -> List[List[int]]:
    '''
    A3 - If sorting is not allowed, how will you track and manage duplication
    '''

    l = len(nums)
    ans=set()
    d1={}
    d3={}

    for k in range(l-2):

        if nums[k] not in d1:

            d1[nums[k]]=k
            i=k+1
            d2={}

            while i<l:

                c = -1*nums[k] - nums[i]

                if c in d2 and d2[c] != i:
                    # x = [nums[k],c,nums[i]]
                    # x.sort()

                    # if x not in d3:
                    # ans.append(x)

                    # This is a very important trick
                    x = (nums[k],c,nums[i])
                    ans.add(tuple(sorted(x)))

                else:
                    d2[nums[i]]=i

                i+=1



        # else:
        #     d1[nums[k]]=k
    return ans


'''
Test Cases
[-1,0,1,2,-1,-4,2]
[-4,2,2]
[0,0,0]
[0,0,0,0]

How to track duplicate lists in a set?
x = (nums[k],c,nums[i])
ans.add(tuple(sorted(x)))
'''

def p1(self, nums: List[int]) -> List[List[int]]:
    '''
    TypeError: unhashable type: 'list'
    '''
    '''
    TC = n^2
    SC = n
    '''
    i = 0
    n = len(nums)
    ans = set()

    while i < n:

        d1 = {}
        j = 0

        while j < n and i != j:

            c = (nums[i]+nums[j])*-1

            if c in d1 and d1[c] != i and d1[c] != j:
                ans.add(tuple(sorted([nums[i], nums[j], c])))
            else:
                d1[nums[j]]=j

            j+=1

        i+=1

    return list(ans)

def p2(self, nums: List[int]) -> List[List[int]]:

    n = len(nums)
    nums.sort()
    k = 0
    ans = []
    last_k = nums[0]-1

    if n == 0:
        return []

    while k < n-2:

        if nums[k] == last_k:
            k+=1
            continue

        i = k+1
        j = n-1

        while i < j:

            s = nums[k] + nums[i] + nums[j]

            if s < 0:
                i+=1
            elif s > 0:
                j-=1
            else:
                x = [nums[k], nums[i], nums[j]]

                ans.append(x)

                i+=1
                j-=1

                while i < j and nums[i]==nums[i-1]:
                    i+=1

        last_k = nums[k]
        k+=1

    return ans
            

'''Adding all this while conditions increases time'''
                
#             if total < 0:
#                 while i < j and nums[i] == second:
#                     i += 1
#             elif total > 0:
#                  while i < j and nums[j] == third:
#                     j -= 1
#             else:
#                 ans.append([first, second, third])
                
#                 while i < j and nums[i] == second:
#                     i += 1
                
#                 while i < j and nums[j] == third:
#                     j -= 1
                
                
                
                
                
                
                
                
                
                
    