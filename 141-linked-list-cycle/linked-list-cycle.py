# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Check if the head is None or if there's only one node in the list
        if not head or not head.next:
            return False

        # Initialize two pointers: slow and fast
        slow = head
        fast = head.next

        # Loop until the pointers meet (indicating a cycle) or reach the end of the list
        while slow != fast:
            # Check if either fast or fast.next is None, which would indicate the end of the list
            if not fast or not fast.next:
                return False

            # Move the slow pointer one step forward and the fast pointer two steps forward
            slow = slow.next
            fast = fast.next.next
        
        # If the loop terminates, it means the pointers have met, indicating the presence of a cycle
        return True
