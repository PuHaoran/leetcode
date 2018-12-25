class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0

        flag = 0
        t = -1
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    break
                if j + 1 == len(needle):
                    flag = 1
            if flag:
                t = i
                break
        return t

'''
题解:
采用暴力遍历方法解答，还有很大的优化空间。
'''