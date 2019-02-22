"""
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
    Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        h = ListNode(0)
        q = h
        h.next = head
        p = h.next
        while p!=None:
            if p.next == None:
                break
            else:
                h.next = p.next
                p.next = p.next.next
                h.next.next = p
                h = p
                p = h.next
        return q.next