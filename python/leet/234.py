# Definition for singly-linked list.
import math

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        val_list = []
        pointer = head

        while pointer != None:
            val_list.append(pointer.val)
            pointer = pointer.next
        
        size = len(val_list)

        result = True
        for i in range(math.ceil(size/2)):
            if val_list[i] != val_list[size - i - 1]:
                result = False
                break
        
        return result