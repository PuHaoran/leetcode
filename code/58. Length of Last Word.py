class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                t = i
                break
        cnt = 0
        for j in range(0, i + 1):
            if s[j] == ' ':
                cnt = 0
            else:
                cnt += 1
        return cnt

'''
题解:
考察字符串
'''