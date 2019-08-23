'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None and n == 1:
            return None

        node = head
        node2 = node
        i = 1
        j = 1
        while (node2.next != None):
            if i - j == n:
                j += 1
                node = node.next
            i += 1
            node2 = node2.next
        if i == n:
            head = head.next
        else:
            node.next = node.next.next

        return head

'''
题解：
删除链表的倒数第n个节点。
指定两个指针，一个指针先行，当两指针之间的差为n时，另一个指针开始计数。注意：需要考虑删除的点在开头的情况。
'''