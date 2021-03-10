from collections import deque


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        self.__deque(arr)

    def __deque(self, arr: List[int]) -> None:
        """
        Time: O(n)
        Space: O(n)
        """
        queue = deque()
        for i, n in enumerate(arr):
            queue.appendleft(n)
            if n == 0:
                queue.appendleft(n)
            arr[i] = queue.pop()
