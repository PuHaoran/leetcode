'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。

如果是则返回true，否则返回false。

假设输入的数组的任意两个数字都互不相同。

样例
输入：[4, 8, 6, 12, 16, 14, 10]

输出：true
'''


class Solution:
    def verifySquenceOfBST(self, sequence):
        """
        :type sequence: List[int]
        :rtype: bool
        """
        if len(sequence) == 1:
            return True

        if len(sequence) == 0:
            return True

        t = len(sequence) - 1
        for i in range(len(sequence)):
            if sequence[i] > sequence[t]:
                t = i
                break

        if t == len(sequence) - 1 or t == 0:
            return self.verifySquenceOfBST(sequence[:len(sequence) - 1])

        for i in range(t + 1, len(sequence) - 1):
            if sequence[i] < sequence[len(sequence) - 1]:
                return False

        return self.verifySquenceOfBST(sequence[:t]) and self.verifySquenceOfBST(sequence[t:len(sequence) - 1])

'''
题解：
二叉搜索树成立的条件是：
左子树 < 根 < 右子树
'''