'''
地上有一个 m 行和 n 列的方格，横纵坐标范围分别是 0∼m−1 和 0∼n−1。

一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格。

但是不能进入行坐标和列坐标的数位之和大于 k 的格子。

请问该机器人能够达到多少个格子？

样例1
输入：k=7, m=4, n=5

输出：20
样例2
输入：k=18, m=40, n=40

输出：1484

解释：当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
      但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
注意:

0<=m<=50
0<=n<=50
0<=k<=100
'''


class Solution(object):
    def get_digit_sum(self, d):
        t = 0
        while d:
            t += d % 10
            d /= 10
        return t

    def check_site(self, i, j, threshold):
        if self.get_digit_sum(i) + self.get_digit_sum(j) <= threshold:
            return True
        return False

    def can_search(self, i, j, threshold, rows, cols, mark):
        if i >= 0 and i < rows and j >= 0 and j < cols and self.check_site(i, j, threshold) and mark[i][j] == 0:
            return True
        return False

    def search(self, i, j, threshold, rows, cols, mark):
        count = 0
        xx = [-1, 1, 0, 0]
        yy = [0, 0, -1, 1]
        if self.can_search(i, j, threshold, rows, cols, mark):
            mark[i][j] = 1
            count = 1
            for k in range(len(xx)):
                count += self.search(i + xx[k], j + yy[k], threshold, rows, cols, mark)
                # count = 1 + self.search(i, j-1, threshold, rows, cols, mark) + \
                # self.search(i, j+1, threshold, rows, cols, mark) + \
                # self.search(i-1, j, threshold, rows, cols, mark) + \
                # self.search(i+1, j, threshold, rows, cols, mark)
        return count

    def movingCount(self, threshold, rows, cols):
        """
        :type threshold: int
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0

        mark = [[0] * cols for i in range(rows)]
        return self.search(0, 0, threshold, rows, cols, mark)

