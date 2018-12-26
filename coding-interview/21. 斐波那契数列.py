'''
输入一个整数 n ，求斐波那契数列的第 n 项。

假定从0开始，第0项为0。(n<=39)

样例
输入整数 n=5

返回 5
'''

class Solution(object):
    def Fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0

        a = 0
        b = 1
        i = 1
        while i < n:
            t = b
            b = a + b
            a = t
            i += 1
        return b

'''
题解:
斐波那契，采用递推求解。
'''
