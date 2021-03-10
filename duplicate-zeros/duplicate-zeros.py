from collections import deque


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Time: O(n)
        Space: O(n)
        """
        queue = deque()
        for i, n in enumerate(arr):
            if queue:
                if n == 0:
                    queue.append(n)
                queue.append(n)
                arr[i] = queue.popleft()
            else:
                if n == 0:
                    queue.append(n)