# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        return self.__bruteforce(head)
    
    def __bruteforce(self, head: ListNode) -> int:
        bitpattern = []
        while head:
            bitpattern.append(head.val)
            head = head.next
        return sum(
            2 ** i for i, _ in filter(
                lambda t: t[1] == 1,
                enumerate(reversed(bitpattern))
                
            )
        )
