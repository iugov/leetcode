# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        # 1 - 2 - 6 - 3
        fake_head = ListNode(0, head)
        # 0 - [1] - 2 - 6 - 3
        prev = fake_head # 0
        curr = head # 1
        
        while curr:
            if curr.val == val:
                prev.next = curr.next # fake_head = [2]
            else:
                prev = curr
            curr = curr.next
        
        return fake_head.next
