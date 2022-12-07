---
date: 2022.12.06
title: 938. Range Sum of BST
runtime: 77.42 # faster than (in %)
memory usage: 17.70 # less than (in %)

---
## Description
Given the `root` node of a binary search tree and two integers `low` and `high`, return *the sum of values of all nodes with a value in the **inclusive** range* `[low, high]`.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg](https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg)

```
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg](https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg)

```
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 2 * 104]`.
- `1 <= Node.val <= 105`
- `1 <= low <= high <= 105`
- All `Node.val` are **unique**.

## Approach 1 : DFS
- Time complexity: `O(n)`
- Space complexity: `O(n)` <br />
where `n` is the number of nodes
``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def DFS(root):
            if root is None:
                return 0
            if root.val <= high and root.val >= low:
                return root.val + DFS(root.left) + DFS(root.right)
            elif root.val < low:
                return DFS(root.right)
            elif root.val > high:
                return DFS(root.left)

        return DFS(root)
