'''
给定一棵二叉树的其中一个节点，请找出中序遍历序列的下一个节点。

注意：

如果给定的节点是中序遍历序列的最后一个，则返回空节点;
二叉树一定不为空，且给定的节点一定不是空节点；
样例
假定二叉树是：[2, 1, 3, null, null, null, null]， 给出的是值等于2的节点。

则应返回值等于3的节点。

解释：该二叉树的结构如下，2的后继节点是3。
  2
 / \
1   3
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.father = None
class Solution(object):
    def inorderSuccessor(self, q):
        """
        :type q: TreeNode
        :rtype: TreeNode
        """
        while 1:
            if q.left == None and q.right == None:
                return q.left
            if q.right != None:
                cur = q.right
                while cur.left != None:
                    cur = cur.left
                return cur
            else:
                if q.father == None:
                    return q.father
                if q.father.left == q:
                    return q.father
                else:
                    cur = q.left
                    while cur.left != None:
                        cur = cur.left
                    return cur

'''
题解：
一道考察树遍历的题，对树不仔细思考还真做不出来。很有意思的一道题。
总共可分为三种情况
1）node有右子树，则最左子节点就是node的下一个节点
2）node有左子树，若node是父节点的左子节点，则下一个节点是父节点
3）node有左子树，若node是父节点的右子节点，最下一个节点是node的最左下节点
要注意边界条件：node无左右子树，和node有左子树且无父节点的情况，这时node为中序遍历最后一个
'''