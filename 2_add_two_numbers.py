"""
https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """ 
        b = 0
        r = ListNode(0)
        m = r
        m.val = l1.val+l2.val+b
        if(m.val >= 10):
            m.val-=10
            b=1
        else:
            b=0
        l1 = l1.next
        l2 = l2.next
        while(l1 !=None and l2 !=None):
            p = ListNode(0)
            m.next = p
            m=p
            m.val = l1.val+l2.val+b
            if(m.val >= 10):
                m.val-=10
                b=1
            else:
                b=0
            l1 = l1.next
            l2 = l2.next
            
        if(l1!= None):
            m.next = l1
            while(l1!=None):
                l1.val += b
                if(l1.val >= 10):
                    l1.val-=10
                    b=1
                else:
                    b=0
                if(l1.next == None and b==1):
                    p = ListNode(1)
                    l1.next = p
                    l1=p
                    b=0
                    break
                l1 = l1.next

            
        elif(l2!= None):
            m.next = l2
            while(l2!=None):
                l2.val += b
                if(l2.val >= 10):
                    l2.val-=10
                    b=1
                else:
                    b=0
                if(l2.next == None and b==1):
                    p = ListNode(1)
                    l2.next = p
                    l2=p
                    b=0
                    break
                l2 = l2.next

        elif(b==1):
            p = ListNode(1)
            m.next = p
            m=p
        return r
