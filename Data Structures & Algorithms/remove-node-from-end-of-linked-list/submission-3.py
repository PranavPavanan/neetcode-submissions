# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        temp, prev = None, head
        leng = head
        count = 0

        while leng:
            count += 1
            leng = leng.next

        target = count - n

        if target == 0:
            return head.next
        
        for i in range(target-1):
            curr = curr.next
        curr.next = curr.next.next
        
        return head

        