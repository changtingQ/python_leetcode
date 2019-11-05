def reversed(x):
    x = -int(str(x[::-1][-1])) if x < 0 else int(str(x)[::-1])
    x = 0 if abs(x) > 0x7FFFFFFF else x
    return x

print(reversed(789))























"-------------------answer--------------------"
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = -int(str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])   # [:-1]相当于把负号去掉
        x = 0 if abs(x) > 0x7FFFFFFF else x
        return x

solution = Solution()
result = solution.reverse(x=98)
print(result)