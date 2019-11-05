def two(nums, target):
    key_word = {}
    for i, num in enumerate(nums):
        if target - num in key_word:
            return key_word[target - num], i
        key_word[target-num] = i
        return []


result = two(nums=[1, 2, 3, 4, 5], target=5)
print(result)





















"------------------------------answer-------------------------------"

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num],i]
            lookup[num] = i
        return []


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
a = solution.twoSum(nums=nums, target=target)
print(a)