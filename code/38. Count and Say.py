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