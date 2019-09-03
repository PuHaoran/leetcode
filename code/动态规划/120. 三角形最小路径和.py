'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        a = [[0 for i in range(n)] for j in range(n)]
        a[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(0, i+1):
                if j == 0:
                    a[i][j] = a[i-1][j] + triangle[i][j]
                elif j == i:
                    a[i][j] = a[i-1][j-1] + triangle[i][j]
                else:
                    a[i][j] = min(a[i-1][j] + triangle[i][j], a[i-1][j-1] + triangle[i][j])
        return min(a[n-1])

''' 
题解
解法一：
递推解法，最容易想到的一种解法，编程将大脑中的思路实现。

解法二：
自顶向下，递推解法。可以利用triangle自己的空间。
'''


