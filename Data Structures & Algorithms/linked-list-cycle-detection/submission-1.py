# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        done = list()

        count == 0
        while head != None:
            if head in done:
                return True
            done.append(head)
            head = head.next

        return False