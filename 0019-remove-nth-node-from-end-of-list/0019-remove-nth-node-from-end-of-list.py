# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head: 
            return head.next
        current = head
        counter = 0
        while current:
            current = current.next
            counter += 1
        if countter == n:
            return head.next 
            
        pos = counter - n -1
        current = head
        for _ in range(pos):
            current = current.next
        
        start = current

        if start.next:
            start.next = start.next.next

        return head
