class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return self.__twopointer(nums)

    def __naive(self, nums: List[int]) -> List[int]:
        return sorted(n * n for n in nums)

    def __twopointer(self, nums: List[int]) -> List[int]:
        result = []
        
        i = 0
        j = len(nums) - 1
        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                result.append(nums[i] ** 2)
                i += 1
            else:
                result.append(nums[j] ** 2)
                j -= 1
        
        return reversed(result)