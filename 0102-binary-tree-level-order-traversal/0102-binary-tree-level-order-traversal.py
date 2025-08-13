'''
Level Order Traversal means BFS (Breadth First Search). BFS is done using queue.
'''
'''
[3,9,20,null,null,15,7]
[1]
[]
'''
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return aug13_25(root)

def aug12_25(root):
    '''BFS, TC = n, SC = n'''

    levels = []

    if root is None:
        return levels

    q = deque()
    q.append(root)
    level = 0

    while q:

        level_len = len(q)
        levels.append([])

        for _ in range(level_len):

            node = q.popleft()

            levels[level].append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        level += 1

    return levels


def aug13_25(root):

    levels = []

    if root is None:
        return levels

    def helper(node, depth):

        if len(levels) == depth:
            levels.append([])

        levels[depth].append(node.val)

        if node.left:
            helper(node.left, depth + 1)
        if node.right:
            helper(node.right, depth + 1)

    helper(root, 0)

    return levels

        



    
def max_depth(root):
    
    if root is None:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))

'''This is DFS not BFS'''
def ans2(root, levels=None, idx = 0):
    if levels is None:
        levels = [None]*max_depth(root)
    if root is None:
        return
    
    if levels[idx] is None:
        levels[idx] = [root.val]
    else:
        levels[idx] += [root.val]
        
    ans2(root.left, levels, idx + 1)
    ans2(root.right, levels, idx + 1)
    return levels

'''Does not work'''
def e1(root):

    if root is None:
        return 
    
    level = []

    ans1(root.left)
    ans1(root.right)
    
    return

def ans1(root):
    
    ans = []
    q = deque()
    
    if root:
        q.append(root)
        
        while q:

            x = []

            for i in range(len(q)):
                node = q.popleft()

                x.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(x)
    
    return ans

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

		ans.append(level_elements)

	return ans
            
    
    