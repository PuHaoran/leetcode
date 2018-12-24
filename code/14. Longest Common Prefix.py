class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        min_len = len(strs[0])
        for s in strs[1:]:
            if len(s) < min_len:
                min_len = len(s)
        res = ''
        for i in range(min_len):
            flag = 0
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j - 1][i]:
                    flag = 1
                    break
            if flag == 0:
                res += strs[0][i]
            else:
                return res
        return res

'''
题解：
考察数组的使用
'''