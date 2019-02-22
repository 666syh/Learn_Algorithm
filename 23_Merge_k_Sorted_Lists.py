"""
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
    Input:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
将数组分为两半，对每半进行合并
"""
class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        
        def recursion(lists: 'List[ListNode]'):
            k = len(lists)
            if k == 0:
                return None
            #如果长度为1，不动
            elif k == 1:
                return lists[0]
            #如果长度为2，进行合并
            elif k == 2:
                p, q = lists[0], lists[1]
                l = ListNode(0)
                h = l
                while p!=None and q!=None:
                    if p.val <= q.val:
                        h.next = p
                        p = p.next
                    else:
                        h.next = q
                        q = q.next
                    h = h.next
                if p!=None:
                    h.next = p
                elif q!=None:
                    h.next = q
                return l.next
            #否则接着分割
            else:
                return recursion([recursion(lists[:k//2]),recursion(lists[k//2:k])])
        return recursion(lists)

