---
date: 2022.01.10
title: 100. Same Tree
runtime: 35 # faster than (in %)
memory usage: 27 # less than (in %)
---

## Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```
Input: p = [1,2,3], q = [1,2,3]
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

```
Input: p = [1,2], q = [1,null,2]
Output: false

```

**Example 3:**

![https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

```
Input: p = [1,2,1], q = [1,1,2]
Output: false

```

**Constraints:**

- The number of nodes in both trees is in the range `[0, 100]`.
- `104 <= Node.val <= 104`

# Approach 1 : Recursive
- Time complexity: `O(n)`
- Space complexity: `O(n)`<br />
where `n` is the number of nodes.
``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        if p and q:
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return p is q
```
```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;

        return isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
    }
}
