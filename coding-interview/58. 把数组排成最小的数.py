'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

例如输入数组[3, 32, 321]，则打印出这3个数字能排成的最小数字321323。

样例
输入：[3, 32, 321]

输出：321323
注意：输出数字的格式为字符串。
'''


class Solution(object):
    def printMinNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                s1 = str(nums[i]) + str(nums[j])
                s2 = str(nums[j]) + str(nums[i])
                if int(s1) > int(s2):
                    t = nums[j]
                    nums[j] = nums[i]
                    nums[i] = t

        return ''.join(map(str, nums))

'''
题解：
类似冒泡排序，根据两两数拼接后的数的大小判断时候需要交换这两个数的位置
'''

