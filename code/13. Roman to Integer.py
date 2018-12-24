class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        for i in range(1, len(s)):
            if d[s[i]] > d[s[i-1]]:
                res += -d[s[i-1]]
            else:
                res += d[s[i-1]]
        res += d[s[len(s)-1]]
        return res

'''
题解：
考察字典的应用
'''