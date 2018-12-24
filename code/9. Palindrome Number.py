class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_copy = x
        if x < 0:
            return False
        s = 0
        while 1:
            s = s*10 + x%10
            x = x//10
            if x == 0:
                break
        if s == x_copy:
            return True
        return False

'''
题解：
考察数字的反转
'''