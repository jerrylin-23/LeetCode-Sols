# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return 

        counter = 0 

        current = head

        while current: 
            counter += 1
            current = current.next

        mid = counter // 2

        current = head 
        
        for _ in range(mid):
            current = current.next

        
        start = head
        mid = current.next
        current.next = None

        reverse_head = mid  
        prev = None 

        while reverse_head:
            next_node = reverse_head.next
            reverse_head.next = prev
            prev = reverse_head
            reverse_head = next_node
        
        reverse_head = prev

        first = start
        second = reverse_head

        while second: 
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        