'''
输入一棵二叉树前序遍历和中序遍历的结果，请重建该二叉树。

样例
给定：
前序遍历是：[3, 9, 20, 15, 7]
中序遍历是：[9, 3, 15, 20, 7]

返回：[3, 9, 20, null, null, 15, 7, null, null, null, null]
返回的二叉树如下所示：
    3
   / \
  9  20
    /  \
   15   7
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        root = preorder[0]
        for i in range(len(inorder)):
            if inorder[i] == root:
                break

        node = TreeNode(root)
        node.left = self.buildTree(preorder[1: 1 + i], inorder[0:i])
        node.right = self.buildTree(preorder[1 + i:], inorder[i + 1:])

        return node

'''
题解：
考察重建二叉树的知识点，由前序和中序遍历求出整个二叉树。
应用递归进行求解。
'''