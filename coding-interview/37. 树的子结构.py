'''
输入两棵二叉树A，B，判断B是不是A的子结构。

我们规定空树不是任何树的子结构。

样例
树A：

     8
    / \
   8   7
  / \
 9   2
    / \
   4   7
树B：

   8
  / \
 9   2
返回 true ,因为B是A的子结构。
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def is_subtree(self, root1, root2):
        if root2 == None:
            return True
        if root1 == None:
            return False

        if root1.val == root2.val:
            return self.is_subtree(root1.left, root2.left) and self.is_subtree(root1.right, root2.right)
        else:
            return False

    def hasSubtree(self, pRoot1, pRoot2):
        """
        :type pRoot1: TreeNode
        :type pRoot2: TreeNode
        :rtype: bool
        """
        if pRoot1 == None or pRoot2 == None:
            return False

        return self.is_subtree(pRoot1, pRoot2) or self.hasSubtree(pRoot1.left, pRoot2) or self.hasSubtree(pRoot1.right,
                                                                                                          pRoot2)
'''
多层递归
'''