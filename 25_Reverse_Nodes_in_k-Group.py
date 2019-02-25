"""
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
    Given this linked list: 1->2->3->4->5
    For k = 2, you should return: 2->1->4->3->5
    For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: 'ListNode', k: 'int') -> 'ListNode':
        h = ListNode(0)
        s = h
        h.next = head
        if k==1:
            return s.next
        index = 0
        #先求总体长度，并进行分组
        while h.next!=None:
            index+=1
            h = h.next
        n = index//k
        h = s
        #外层循环-总组数
        for i in range(n):
            p = h.next
            #内层循环-每一组进行交换
            for l in range(1, k):
                q = h.next
                h.next = p.next
                p.next = p.next.next
                h.next.next = q
            h = p
        return s.next
        

