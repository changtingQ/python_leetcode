def remove_element(l1, ele):
    for i in l1:
        if i == ele:
            l1.remove(i)
    return len(l1)

a = remove_element(l1=[1, 2, 3, 3, 3, 4], ele=3)
print(a)
















'-----------------answer----------------'
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)