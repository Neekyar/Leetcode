class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        i = 1
        while 2**i < len(root):
            for j in range(2**(i-1)):
                root[2**i - 1 + j],root[2**i - 1 + 2**(i-1) + j] = root[2**i - 1 + 2**(i-1)+j], root[2**i - 1 + j]

        return root

    
