from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return aug01_25(head)

def aug01_25(head):
    '''TC = n, SC = n'''

    stack = deque()
    t = []

    while head:
        # print(head.val)
        # if stack:
        #     if stack[-1] == head.val:
        #         stack.pop()
        #         head = head.next
        #         continue
        # stack.append(head.val)
        t.append(head.val)
        head = head.next

    i, j = 0, len(t)-1

    while i < j:
        if t[i] != t[j]:
            return False
        i += 1
        j -= 1
    
    return True

'''
[1,2,2,1]
[1,2]
[1]
[1,0,0]
[1,0,1]
'''



def ans(head):
    '''TC=n, SC=1'''
    def reverse(head):
        prev = None
        cur = head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev

    def end_of_first(head):
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow

    first_end = end_of_first(head)
    print(first_end.val)
    second_start = reverse(first_end.next)
    
    result = True
    left = head
    right = second_start
    
    while result and left and right:
        if left.val != right.val:
            result = False
        left = left.next
        right = right.next
        
    first_end.next = reverse(right)
    
    return result
    
    
def ans_sol(head):
    
    def end_of_first_half(head):
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
    
    
    def reverse_linked_list(head):
        prev = None
        cur = head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        return prev
    
    
    if head is None:
        return True
       
    first_half_end = end_of_first_half(head)
    second_half_start = reverse_linked_list(first_half_end.next)
    # print(first_half_end.val, second_half_start.val)
    
    result = True
    first_position = head
    second_position = second_half_start
    
    while result and second_position:
        if first_position.val != second_position.val:
            result = False
        first_position = first_position.next
        second_position = second_position.next
        
    first_position.next = reverse_linked_list(second_half_start)
    return result
    
def ans_fail(head):
    
    x = []
    n = 0
    
    start = ptr = head
    
    
    while ptr:
        x.append(ptr.val)
        n += 1
        ptr = ptr.next
        
    if n == 1:
        return True
    
    mid = n//2 if n % 2 == 0 else (n // 2) + 2

    
    mid_ptr = None
    t = 0
    
    ptr = head
    
    while ptr:
        t += 1
        
        if t == mid:
            mid_ptr = ListNode(ptr.val, ptr.next)
            break
        ptr = ptr.next
    
    i = 0
    
    ptr = head
    while ptr and mid_ptr and i <= mid:
        
        print(ptr.val, mid_ptr.val)
        if ptr.val == mid_ptr.val:
            ptr = ptr.next
            mid_ptr = mid_ptr.next
        else:
            return False
        
        i +=1
    
    return True

'''
[1,2,2,1]
[1,2]
'''
            