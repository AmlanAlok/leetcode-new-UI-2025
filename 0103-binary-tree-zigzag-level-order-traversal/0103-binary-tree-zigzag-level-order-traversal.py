from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return aug16_25(root)

def aug16_25(root):
    '''TC = n, SC = n'''

    if root is None:
        return []
        
    levels = []
    level = 0

    q = deque([root])

    while q:

        level_len = len(q)
        levels.append([])

        for _ in range(level_len):

            node = q.popleft()

            if level % 2 == 0:
                levels[level].append(node.val)
            else:
                levels[level].insert(0, node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        level += 1
    
    return levels

        