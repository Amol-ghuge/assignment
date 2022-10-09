from typing import Optional,List
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
	
        pointer = head
        prev = None
        counter = 0
        while pointer != None:
            if pointer.val in nums:
                if not prev:
                    counter += 1
                prev = True
            else:
                prev = False
            pointer = pointer.next
        return counter
