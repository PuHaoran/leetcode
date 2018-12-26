class Solution:
    def countNum(self, s):
        cnt = 0
        i = 0
        res = ''
        while i < len(s):
            if i == 0 or s[i] == s[i - 1]:
                cnt += 1
            else:
                res += str(cnt) + s[i - 1]
                cnt = 1
            i += 1
            if i == len(s):
                res += str(cnt) + s[i - 1]
        return res

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        arr = ['', '1']
        for i in range(2, 31):
            arr.append(self.countNum(arr[i - 1]))
        return arr[n]

'''
题解:
字符串拼接
'''
import itertools

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ['', '1']
        for i in range(2, 31):
            tmp_str = ''
            for k, g in itertools.groupby(res[i-1]):
                tmp_str += str(len(list(g))) + k
            res.append(tmp_str)
        return res[n]

'''
题解:
使用python语法中的tricks，itertools.groupby()把迭代器中相邻的重复元素挑出来放在一起。
'''