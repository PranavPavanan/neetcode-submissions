class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node to protect against edge cases (like removing the head)
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # 2. Move the right pointer forward 'n' times to create the gap
        for _ in range(n):
            right = right.next
            
        # 3. Move both pointers together until 'right' hits the end of the list
        while right:
            left = left.next
            right = right.next
            
        # 4. 'left' is now sitting right before the node we want to delete.
        # We delete it by routing left's arrow AROUND the target node.
        left.next = left.next.next
        
        # Return the true head (skipping the dummy)
        return dummy.next