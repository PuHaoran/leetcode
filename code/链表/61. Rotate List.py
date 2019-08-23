'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node = head
        num = 0
        while node != None:
            num += 1
            node = node.next

        if num == 0:
            return head
        k = k % num
        if k == 0:
            return head

        i = 1
        j = 1
        node = head
        node2 = head
        while node.next != None:
            if i - j == k:
                j += 1
                node2 = node2.next
            i += 1
            node = node.next
        node.next = head
        head = node2.next
        node2.next = None

        return head

'''
题解：
和第19题的解法类似。找到两个指针，一个指针先行，然后一个指针在j-i=n的时候开始行进。
注意边界条件的判断。
'''