class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s2 = []
        d = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for i in range(len(s)):
            if len(s2) == 0:
                s2.append(s[i])
            elif s[i] in d and s2[-1] == d[s[i]]:
                s2 = s2[0:-1]
            else:
                s2.append(s[i])
        if len(s2)==0:
            return True
        return False

'''
题解：
考察栈的使用
'''