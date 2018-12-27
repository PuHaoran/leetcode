'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。

请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

样例
输入数组：

[
  [1,2,8,9]，
  [2,4,9,12]，
  [4,7,10,13]，
  [6,8,11,15]
]

如果输入查找数值为7，则返回true，

如果输入查找数值为5，则返回false。
'''


class Solution(object):
    def searchArray(self, array, target):
        """
        :type array: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if array == []:
            return False

        i = 0
        j = len(array[0]) - 1
        while 1:
            if j < 0 or i > len(array) - 1:
                return False
            if array[i][j] == target:
                return True
            if target < array[i][j]:
                j -= 1
            elif target > array[i][j]:
                i += 1

'''
题解：
考察从简单到复杂的解题思路。当问题很复杂时要尝试从最简单的情况开始考虑，逐渐慢慢推导。
PS：注意边界条件，输入存在字符串要考虑空串情况，输入存在数组要考虑空数组情况。
'''

