# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return aug02_25(head)
    
    def ans_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        c = head
        
        while c:
            t = c.next
            c.next = prev
            prev = c
            c = t
        
        return prev
    
    def ans_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = head
        c = head.next
        
        while c:
            if c.next != None:
                t = c.next
                c.next = prev
                prev = c 
                c = t
            else:
                c.next = prev
                break
            
        return c

def aug02_25(head):

    prev = None
    cur = head

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    
    return prev

        