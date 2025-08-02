'''
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
["MinStack","push","push","getMin","getMin","push","getMin","getMin","top","getMin","pop","push","push","getMin","push","pop","top","getMin","pop"]
[[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]
'''
from collections import deque
import sys

class MinStack:

    def __init__(self):
        self.s = deque()
        self.minV = sys.maxsize

    def push(self, val: int) -> None:
        if val < self.minV:
            self.minV = val
        self.s.append((val, self.minV))

    def pop(self) -> None:
        self.s.pop()
        
        '''Both these lines save you from edge cases'''
        if len(self.s) == 0:
            self.minV = sys.maxsize
        else:
            self.minV = self.s[-1][1]
            
    def top(self) -> int:
        return self.s[-1][0]
        
    def getMin(self) -> int:
        return self.s[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()