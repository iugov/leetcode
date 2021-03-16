class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return self.__other(nums, n)

    def __first(self, nums: List[int], n: int) -> List[int]:
        result = []
        j = n
        for i in range(2 * n):
            if i % 2 == 0:
                result.append(nums[i // 2])
            else:
                result.append(nums[j])
                j += 1
        return result
    
    def __other(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])
        return result
        