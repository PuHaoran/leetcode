'''
定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。

样例
输入:1->2->3->4->5->NULL

输出:5->4->3->2->1->NULL
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        new_head = ListNode(head.val)
        head = head.next
        while head != None:
            node = ListNode(head.val)
            node.next = new_head
            new_head = node

            head = head.next
        return new_head

'''
链表
'''