# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:31:49 2020

@author: renli
"""
def deleteDuplicates(head):
    if head is None: return None
    memo = {}
    memo[head.data] = True
    curr = head
    while curr.next is not None:
        if curr.next.data in memo:
            curr.next = curr.next.next
        else:
            memo[curr.next.data] = True
            curr = curr.next
    return head

if __name__=="__main__":
    pass