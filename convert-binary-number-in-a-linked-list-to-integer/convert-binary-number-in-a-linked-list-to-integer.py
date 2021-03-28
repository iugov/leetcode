# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        return self.__constspace2(head)

    def __constspace2(self, head: ListNode) -> int:
        result = head.val
        while head.next:
            result = (result << 1) | head.next.val
            head = head.next
        return result
    
    def __constspace(self, head: ListNode) -> int:
        result = head.val
        while head.next:
            result = result * 2 + head.next.val
            head = head.next
        return result

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
