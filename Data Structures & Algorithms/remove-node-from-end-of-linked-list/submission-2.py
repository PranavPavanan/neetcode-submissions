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

        i = 0
        while curr:
            temp = curr.next
            if i == target:
                curr.next = None
                prev.next = temp
                return head

            prev = curr
            curr = temp
            i += 1
        prev = head
        
        prev.next = None
        return head

        