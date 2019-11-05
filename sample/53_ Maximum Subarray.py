def find_max_num(ll):
    for i in range(1, len(ll)):
        ll[i] = ll[i] + max(ll[i-1], 0)
    return max(ll)




a = find_max_num([1, -3, 5, -6])
print(a)


















"------------------answer-------------------思考1"

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        print(nums)
        return max(nums)
# solution = Solution()
# a = solution.maxSubArray([1, 3, 5, 6])
# print(a)


"-------------------answer-------------------思路2"

class Solution:
    def maxSubArray(self, nums):
        length = len(nums)
        memory = []
        max_val = nums[0]
        sub_list = []
        for x1 in range(length):
            memory.append([])
            for x2 in range(length):
                memory[x1].append(nums[x2])
                if x2 > x1:
                    memory[x1][x2] = memory[x1][x2-1] + nums[x2]
                if memory[x1][x2] > max_val:
                    max_val = memory[x1][x2]
                    sub_list = nums[x1:x2+1]

        print(sub_list)
        return max_val
solution = Solution()
a = solution.maxSubArray([1, 3, 5, 6])
print(a)
