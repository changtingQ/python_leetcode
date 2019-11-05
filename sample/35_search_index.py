def find_index(l1, num_1):
    if num_1 in l1:
        return l1.index(num_1)
    elif num_1 not in l1:
        l1.append(num_1)
        l1.sort()
        return l1.index(num_1)

# a = find_index([1, 2, 3, 4, 9], 5)
# print(a)


def er_fen(l1: list, num_1: str):
    low = 0
    high = len(l1)
    while low < high:
        mid = (low + high) // 2
        if l1[mid] > num_1:
            high = mid
        elif l1[mid] < num_1:
            low = mid + 1
        else:
            return mid
    return low

a = er_fen([1, 2, 3, 4, 9], 5)
print(a)



'-----------------------answer------------------------'
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