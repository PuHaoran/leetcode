'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序。

使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分。

样例
输入：[1,2,3,4,5]

输出: [1,3,5,2,4]
'''

class Solution(object):
    def reOrderArray(self, array):
        """
        :type array: List[int]
        :rtype: void
        """
        left = 0
        right = len(array) - 1

        while left < right:
            while left < right and array[left] & 1:
                left += 1
            while left < right and not array[right] & 1:
                right -= 1
            if left < right:
                t = array[left]
                array[left] = array[right]
                array[right] = t
        return array

