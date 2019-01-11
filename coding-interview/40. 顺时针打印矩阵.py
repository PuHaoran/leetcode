'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

样例
输入：
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

输出：[1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution(object):
    def check_step(self, mark, i, j):
        row = len(mark)
        column = len(mark[0])
        if i < row and j < column and i >= 0 and j >= 0:
            if mark[i][j] == 0:
                return True
        return False

    def printMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        t = 0  # 步数
        flag = 1  # 记录方向
        row = len(matrix)
        if row == 0:
            return []
        column = len(matrix[0])
        if column == 0:
            return []

        mark = [[0] * column for i in range(row)]
        count = row * column

        i, j = 0, 0
        res = [matrix[0][0]]
        mark[0][0] = 1

        while len(res) < count:
            if flag == 1:
                if self.check_step(mark, i, j + 1):
                    j += 1
                    res.append(matrix[i][j])
                    mark[i][j] = 1
                else:
                    flag = 2
            elif flag == 2:
                if self.check_step(mark, i + 1, j):
                    i += 1
                    res.append(matrix[i][j])
                    mark[i][j] = 1
                else:
                    flag = 3
            elif flag == 3:
                if self.check_step(mark, i, j - 1):
                    j -= 1
                    res.append(matrix[i][j])
                    mark[i][j] = 1
                else:
                    flag = 4
            elif flag == 4:
                if self.check_step(mark, i - 1, j):
                    i -= 1
                    res.append(matrix[i][j])
                    mark[i][j] = 1
                else:
                    flag = 1
        return res

'''
每前进一步进行一次检查，用一个mark矩阵标记走过的步数。
'''