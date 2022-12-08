---
date: 2022.12.08
title: 872. Leaf-Similar Trees
runtime: 99.26% # faster than (in %)
memory usage: 87.58%    # less than (in %)
---

## Description
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a **leaf value sequence***.*

![https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png)

For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.

Two binary trees are considered *leaf-similar* if their leaf value sequence is the same.

Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg)

```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg)

```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

```

**Constraints:**

- The number of nodes in each tree will be in the range `[1, 200]`.
- Both of the given trees will have values in the range `[0, 200]`.


## 1st Approchach : DFS
- Time complexity: `O(n+m)`
- Space complexity: `O(n+m)` <br />
where `n` is the number of nodes in `root1` and `m` the number of nodes in `root2`.

**Explanation** Inorder DFS's traversal rule (left node, current node, right node) fit this problem.

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = []
        seq2 = []
        def dfs(root,seq):
            if root:
                dfs(root.left,seq)

                if root.left is None and root.right is None:
                    seq.append(root.val)
                
                dfs(root.right,seq)
        
        dfs(root1,seq1)
        dfs(root2,seq2)

        return seq1 == seq2
```
