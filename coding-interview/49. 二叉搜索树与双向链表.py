'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。

要求不能创建任何新的结点，只能调整树中结点指针的指向。

注意：

需要返回双向链表最左侧的节点。
例如，输入下图中左边的二叉搜索树，则输出右边的排序双向链表。
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.list_head = None
        self.list_tail = None

    def convert(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        self.convert(root.left)
        if self.list_head == None:
            self.list_head = root
            self.list_tail = root
        else:
            self.list_tail.right = root
            root.left = self.list_tail
            self.list_tail = root
        self.convert(root.right)
        return self.list_head

'''
题解：
中序遍历的做法，需要注意双向链表的构建过程，由于最后需要从头结点开始遍历链表，故设置一个头结点，一个尾结点。
'''