def merge_sort_arry(l1: list, m: int, l2: list, n: int):
    while m > 0 and n > 0:
        if l1[m-1] > l2[n-1]:
            l1[m+n-1] = l1[m-1]
            m -= 1
        else:
            l1[m+n-1] = l2[n-1]
            n -= 1
    if n > 0:
        l1[:n] = l2[:n]



l1 = [1, 3, 4, 5, 6, 7, 9, 10]
l2 = [1, 5, 7, 9]
result = merge_sort_arry(l1=l1, m=8, l2 = l2, n=4)
print(result)











print("-----------------answer-----------------思路1")
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        c = 0    # 计数nums1中不需要进行移动的元素的个数
        for i in range(n):
            while j<(m+n):
                if nums1[j] > nums2[i]:
                    nums1[j+1:m-c+j+1] = nums1[j:m-c+j]
                    nums1[j] = nums2[i]
                    j += 1
                    break
                else:
                    c += 1
                    j += 1
            else:
                nums1[m+i] = nums2[i]
l1 = [1, 3, 4, 5, 6, 7, 9, 10]
l2 = [1, 5, 7, 9]
solution = Solution()
result = solution.merge(nums1=l1, m=7, nums2=l2, n=3)
print(result)