# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.depth(root)
        return self.res
    def depth(self,root):
        if root is None:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        self.res = max(self.res,l+r)
        return max(l,r) + 1
