from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return self.__comb(nums)

    def __naive(self, nums: List[int]) -> int:
        """
        Time: O(n^2)
        Space: O(1)
        """
        result = 0
        for j in range(len(nums)):
            for i in range(j):
                if i != j and nums[i] == nums[j]:
                    result += 1
        return result

    def __comb(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        result = 0
        for n in Counter(nums).values():
            if n > 1:
                result += n * (n - 1) // 2
        return result
