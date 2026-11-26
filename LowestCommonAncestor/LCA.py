
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #recurisve dfs method
        #base case

        if not root or root == p or root == q:
            return root
        #left part search
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q) #right part serach

        if left and right:
            return root #we found LCA
        return left if left else right # if we found only one value
