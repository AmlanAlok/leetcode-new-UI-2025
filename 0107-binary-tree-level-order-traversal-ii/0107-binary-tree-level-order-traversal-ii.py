# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
[3,9,20,null,null,15,7]
[1]
[]
'''
from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        return sol(root)
    
    
def sol(root):

	ans = []

	if root is None:
		return ans

	stack = deque()
	stack.append(root)

	while stack:

		level_size = len(stack)
		level_elements = []

		for _ in range(level_size):

			current = stack.popleft()

			children = [current.left, current.right]

			for child in children:
				if child:
					stack.append(child)

			level_elements.append(current.val)

		ans.insert(0, level_elements)

	return ans