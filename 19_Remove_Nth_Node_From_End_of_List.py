"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        index = 0
        t = head
        #先判断链表长度
        while t!=None:
            t = t.next
            index+=1
        #找到并链接
        if n == index:
            head = head.next
        else:
            h = head
            for i in range(index):
                if i == index-n-1:
                    break
                h = h.next
            h.next = h.next.next
        return head
            