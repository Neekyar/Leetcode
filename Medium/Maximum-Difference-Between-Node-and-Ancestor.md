---
date: 2022.12.09
title: 1026. Maximum Difference Between Node and Ancestor 
tags: 
  - DFS
  - Top-bottom
  - Bottom-up
---

## Description
Given the `root` of a binary tree, find the maximum value `v` for which there exist **different** nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor of `b`.

A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b` or any child of `a` is an ancestor of `b`.

**Example 1:**


![https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg)

```
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg)

```
Input: root = [1,null,2,null,0,3]
Output: 3

```

**Constraints:**

- The number of nodes in the tree is in the range `[2, 5000]`.
- `0 <= Node.val <= 105`

## 1st Approach : Bottom-up (post-order DFS)
- Recurse the left and righ subtree to find the max and min value of the children of each subtree
- Then `ans` it will update as `max(ans, root.value - curMin, curMax - root.value)` to get the maximum absolute difference
- We return the `curMax` and `curMin` value of this subtree to the node above 

``` python
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root: return inf, -inf
            leftMin, leftMax = dfs(root.left)
            rightMin,rightMax = dfs(root.right)
            value = root.val
            curMin = min(value,leftMin,rightMin)
            curMax = max(value,leftMax,rightMax)
            self.ans = max(self.ans, value - curMin,curMax - value)
            return curMin,curMax
        dfs(root)
        return self.ans
        
```

## 2nd Approach : Top-bottom (pre-order DFS)
We keep track of the min and max value of the ancestor nodes as we visit each subtree.

- update the curMin` and `curMax` value by checking the current node value
- update `ans` value 
- Recurse the left and right subtree
``` python
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root,curMin,curMax):
            if root:
                value = root.val
                curMin = min(value,curMin)
                curMax = max(value,curMax)
                self.ans = max(self.ans, value - curMin,curMax-value)
                dfs(root.left,curMin,curMax)
                dfs(root.right,curMin,curMax)
                
        dfs(root,root.val,root.val)
        return self.ans
