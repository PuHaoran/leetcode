'''
547. Friend Circles
Medium

1141

94

Favorite

Share
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
'''

class Solution:
    def __init__(self):
        self.pre = collections.defaultdict(int)
        self.res = set()

    def findCircleNum(self, M: List[List[int]]) -> int:
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    self.union(i, j)

        return len(self.res)

    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root != b_root:
            self.pre[a_root] = b_root
            if a_root in self.res:
                self.res.remove(a_root)
        self.res.add(b_root)

    def find(self, root):
        ''' 找根节点 '''
        while root in self.pre:
            root = self.pre[root]
        return root

'''
题解：
经典并查集问题，没有参考代码，一次AC，哈哈这感觉不错。
找朋友圈子，其实可以理解为统计最后根节点的个数。这里我用一个集合存储根节点，如果有合并就把非根节点元素从集合中移除。
'''