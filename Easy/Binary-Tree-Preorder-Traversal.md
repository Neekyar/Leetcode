---
date: 2022.01.09
title: 144. Binary Tree Preorder Traversal
runtime: 85 # faster than (in %)
memory usage: 57 # less than (in %)
---

Given the `root` of a binary tree, return *the preorder traversal of its nodes' values*.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```
Input: root = [1,null,2,3]
Output: [1,2,3]

```

**Example 2:**

```
Input: root = []
Output: []

```

**Example 3:**

```
Input: root = [1]
Output: [1]

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `100 <= Node.val <= 100`

# Approach 1 : Recursion
- Time complexity: `O(n)`
- Space complexity: `O(n)`<br />
where `n` is the number of nodes
``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.dfs(root,ans)
        return ans


    def dfs(self,root, ans):
        if root:
            ans.append(root.val)
            self.dfs(root.left,ans)
            self.dfs(root.right,ans)
```
