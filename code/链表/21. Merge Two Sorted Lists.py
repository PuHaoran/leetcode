# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0)
        cur = head

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        if l1 == None:
            cur.next = l2
        if l2 == None:
            cur.next = l1
        return head.next

'''
题解：
易懂的解法，开辟一个新链表，比较两个链表较小的元素赋给新链表。
若一个链表先到末尾，则将另一个链表值全部赋给新链表。
需要注意python变量赋值的问题。在python中变量可分为可变变量和不可变变量。
像[]、{}、类变量等大多数变量是可变变量，字符串变量赋值是不可变变量。
'''