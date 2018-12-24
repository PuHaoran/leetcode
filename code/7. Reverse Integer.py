class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
            x = -x
            flag = 1
        s = 0
        while 1:
            s = s*10 + x%10
            x = x//10
            if x == 0:
                break
        if flag:
            s = -s
        if s < 2147483648 and s > -2147483648:
            return s
        else:
            return 0
'''
题解：
注意前面所说的有符号32位整型int，反转后的数值不可用大于2**31或小于-2**31
'''