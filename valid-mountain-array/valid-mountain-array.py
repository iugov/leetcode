class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(1)
        
        1.68 ms ± 9.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
        """
        if len(arr) < 3:
            return False

        i = 0

        # Climbing strictly up.
        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1
        
        if i == 0 or i == len(arr) - 1:
            return False

        # Climbing strictly down.
        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            i += 1
        
        return True if i == len(arr) - 1 else False
