# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return aug16_25(root)


def aug16_25(root):
    '''TC = n log(n), SC = n'''

    def helper(node, path):
        
        path += str(node.val)

        if node.left is None and node.right is None:
            paths.append(path)
        if node.left:
            helper(node.left, path + '->')
        if node.right:
            helper(node.right, path + '->')

    paths = []

    if root:
        helper(root, '')
    
    return paths


# def aug16_25(root):

#     def helper(node, path):
        
#         # if path is None:
#         #     path = []

#         path.append(str(node.val))

#         if node.left is None and node.right is None:
#             paths.append('->'.join(path))
#         if node.left:
#             helper(node.left, path)
#         if node.right:
#             helper(node.right, path)

#     paths = []

#     if root:
#         helper(root, [])
    
#     return paths
    

    

    
    





        