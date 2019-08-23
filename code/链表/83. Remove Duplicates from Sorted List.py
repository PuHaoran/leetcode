'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur != None:
            node = cur.next
            while node != None and node.val == cur.val:
                node = node.next
            cur.next = node
            cur = cur.next
        return head

'''
题解：
删除链表中重复的元素，很经典的链表题，在本子上画画思路就来了。
'''