'''
输入一个整数 n ，求斐波那契数列的第 n 项。

假定从0开始，第0项为0。(n<=39)

样例
输入整数 n=5

返回 5
'''

'''
递推+滚动变量，时间复杂度O(n)，空间复杂度O(1)。
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
递归
计算n^2个节点，时间复杂度O(n^2)
算法题中避免整数溢出，通常要对数据取模10^9+7，这是一个非常大的质数。
为什么要取模？数据比较大时，避免整数溢出。
为什么要是质数？能够保证散列后的数尽量随机均匀分布。
'''
class Solution(object):
    MOD = 10**9+7
    def Fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n >= 2:
            return (self.Fibonacci(n-1) + self.Fibonacci(n-2)) % self.MOD

'''
记忆化搜索
开一个大数组计算中间结果，如果存在，则直接返回结果，否则继续递归。
'''
class Solution(object):
    MOD = 10 ** 9 + 7
    a = [-1] * MOD

    def Fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.a[n] != -1:
            return self.a[n]
        if n == 0:
            return 0
        if n == 1:
            return 1

        self.a[n] = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
        return self.a[n]



