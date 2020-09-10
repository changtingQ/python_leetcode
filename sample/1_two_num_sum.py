def two(nums, target):
    key_word = {}
    for i, num in enumerate(nums):
        if target - num in key_word:
            return key_word[target - num], i
        key_word[target - num] = i
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
                return [lookup[target - num], i]
            lookup[num] = i
        return []


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
a = solution.twoSum(nums=nums, target=target)
print(a)


"------------------------------answer2020。9。10-------------------------------"
"""给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。"""
class Solution:
    def sum(self, nums, target):
        look_up = {}
        for i,num in enumerate(nums):
            if target-num in look_up:
                return look_up[target - num], i
            look_up[num] = i
        return []

