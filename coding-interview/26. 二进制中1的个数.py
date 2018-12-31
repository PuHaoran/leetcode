'''
26. 二进制中1的个数

输入一个整数，输出该数二进制表示中1的个数。

例如，将9表示为二进制是1001，有2位是1，因此，如果输入为9，输出应当为2。

样例
输入：9

输出：2
'''

class Solution(object):
    def NumberOf1(self,n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        if n < 0:
            n = n & 0x7FFFFFFF
            cnt += 1
        while n:
            if n & 1:
                cnt += 1
            n = n >> 1
        return cnt

'''
题解：
考察对二进制的了解，这里用到了位运算操作。
需要注意点是若n为负数，进行右移运算时，它会在左边补一以保证数字为负；所以要先转换为正数再位运算。
'''