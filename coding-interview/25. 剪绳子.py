'''
给你一根长度为 n 绳子，请把绳子剪成 m 段（m、n 都是整数，2≤n≤58 并且 m≥2）。

每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]k[1] … k[m] 可能的最大乘积是多少？

例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到最大的乘积18。

样例
输入：8

输出：18
'''


class Solution(object):
    def maxProductAfterCutting(self, length):
        """
        :type length: int
        :rtype: int
        """
        cut_array = [0] * (length + 4)
        cut_array[0] = 0
        cut_array[1] = 1
        cut_array[2] = 2
        cut_array[3] = 3
        if length < 2:
            return 0
        elif length == 2:
            return 1
        elif length == 3:
            return 2
        else:
            for i in range(4, length + 1):
                max = 0
                for j in range(1, i // 2 + 1):
                    temp = cut_array[j] * cut_array[i - j]
                    if max < temp:
                        max = temp
                cut_array[i] = max

        return cut_array[length]

