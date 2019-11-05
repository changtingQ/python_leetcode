# def del_list_duplicate(l1):
#     ll = []
#     for i in l1:
#         if i not in ll:
#             ll.append(i)
#     return ll
#
# a = del_list_duplicate([1, 3, 5, 6, 7, 7 ,7, 9])
# print(a)

def del_list_duplicate(l1):
    i = 0
    while i < (len(l1) -1):
        if l1[i] == l1[i+1]:
            l1.remove(l1[i])
        else:
            i += 1
    return l1

a = del_list_duplicate([1, 3, 5, 6, 7, 7 ,7, 9])
print(a)




"--------------------answer--------------------"
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < (len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)