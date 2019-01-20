'''
输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。

从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

样例
给出二叉树如下所示，并给出num=22。
      5
     / \
    4   6
   /   / \
  12  13  6
 /  \    / \
9    1  5   1

输出：[[5,4,12,1],[5,6,6,5]]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res_list = []
        self.all_res_list = []

    def get_sum(self, my_list):
        count = 0
        for i in range(len(my_list)):
            count += my_list[i]
        return count

    def search(self, root, sum):
        if root == None:
            return

        self.res_list.append(root.val)

        if self.get_sum(self.res_list) == sum and root.left == None and root.right == None:
            self.all_res_list.append(self.res_list)

        self.search(root.left, sum)
        self.search(root.right, sum)
        # 回溯
        self.res_list = self.res_list[:-1]

    def findPath(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.search(root, sum)
        return self.all_res_list

'''
需要注意的点：
递归中全局变量的设置，回溯的使用。
'''