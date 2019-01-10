'''
输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按照递增排序的。

样例
输入：1->3->5 , 2->4->5

输出：1->2->3->4->5->5
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val <= l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next
        new_l = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                new_l.next = node
                new_l = new_l.next

                l1 = l1.next
            else:
                node = ListNode(l2.val)
                new_l.next = node
                new_l = new_l.next

                l2 = l2.next

        if l1 == None:
            new_l.next = l2
        if l2 == None:
            new_l.next = l1
        return head

'''
链表
'''