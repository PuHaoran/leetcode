'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。

路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。

如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。

注意：

输入的路径不为空；
所有出现的字符均为大写英文字母；
样例
matrix=
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

str="BCCE" , return "true"

str="ASAE" , return "false"
'''


class Solution(object):
    def search(self, matrix, s, i, j):
        if matrix[i][j] == s[0]:
            if len(s[1:]) == 0:
                return True
            # 每次遍历先对当前值赋空
            matrix[i][j] = ''

            # 上
            if i > 0 and self.search(matrix, s[1:], i - 1, j):
                return True
            # 下
            if i < len(matrix) - 1 and self.search(matrix, s[1:], i + 1, j):
                return True
            # 左
            if j > 0 and self.search(matrix, s[1:], i, j - 1):
                return True
            # 右
            if j < len(matrix[0]) - 1 and self.search(matrix, s[1:], i, j + 1):
                return True

            # 回溯为原值
            matrix[i][j] = s[0]
            return False
        else:
            return False

    def hasPath(self, matrix, string):
        """
        :type matrix: List[List[str]]
        :type string: str
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.search(matrix, string, i, j):
                    return True
        return False

'''
题解：
回溯问题，递归的经典应用场景。
'''