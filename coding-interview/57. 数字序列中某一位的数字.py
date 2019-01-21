'''
数字以0123456789101112131415…的格式序列化到一个字符序列中。

在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数求任意位对应的数字。

样例
输入：13

输出：1
'''


class Solution(object):
    def digitAtIndex(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        t = 1
        s = 0
        cur = 0
        while 1:
            if t == 1:
                cur = 10
            else:
                cur = t * 9 * 10 ** (t - 1)
            s += cur
            if s > n:
                st = 10 ** (t - 1)
                if t == 1:
                    st = 0
                ed = 10 ** t - 1

                cur_t = n - (s - cur)
                cur_num = st + cur_t / t
                return str(cur_num)[cur_t % t]
            t += 1

'''
题解：
先找到该任意数对应的位数，然后根据该位数的起始数和位数找到该数的值
'''