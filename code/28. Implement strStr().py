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
时间复杂度O(m*n)
采用暴力遍历方法解答，还有很大的优化空间。
'''

class Solution:
    def get_next(self, needle):
        i = 1
        j = 0
        next = [0] * len(needle)
        while i < len(needle):
            if needle[i] == needle[j]:
                next[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    next[i] = 0
                    i += 1
                else:
                    j = next[j - 1]
        return next

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        next = self.get_next(needle)
        i = 0
        j = 0
        if needle == '':
            return 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if len(needle) == j:
                    return i - j
                    break
            else:
                if j == 0:
                    i += 1
                else:
                    j = next[j - 1]
        return -1

'''
题解:
KMP解法，时间复杂度O(m+n)
算法视频：
https://www.bilibili.com/video/av3246487/?spm_id_from=333.788.videocard.6
'''