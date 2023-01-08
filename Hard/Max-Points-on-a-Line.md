---
date: 2022.01.08
title: 149. Max Points on a Line
runtime: 95 # faster than (in %)
memory usage: 93.93 # less than (in %)
---
## Description
Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return *the maximum number of points that lie on the same straight line*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg](https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg)

```
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg](https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg)

```
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

```

**Constraints:**

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `104 <= xi, yi <= 104`
- All the `points` are **unique**.

# Approach (Python):
- Time complexity : $O(n^2)$

``` python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        point = 1 #initialize at 1 if there is only one point in the array
        for i,p in enumerate(points):
            counts = {}
            x1 = p[0]
            y1 = p[1]
            for tmp in points[i+1:]:
                x2 = tmp[0]
                y2 = tmp[1]
                if (x2 - x1) != 0:
                    slope = (y2 - y1)/(x2 - x1)
                else:
                    slope = 'same x' #if the slope is vertical
                counts[slope] = counts.get(slope, 0) + 1
            for i in counts:
                point = max(point, counts[i] + 1) #+1 bc we have take into account the initial point
                
        return point
```
