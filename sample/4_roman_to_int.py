def roman(x):
    dict_data = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
    res = 0
    for i in range(len(x)):
        if i > 0 and dict_data[x[i]] > dict_data[x[i-1]]:
            res += dict_data[x[i]] - 2 * dict_data[x[i-1]]
        else:
            res += dict_data[x[i]]
    return res

# print(roman("VIII"))










"""-------------------answer---------------------"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        res = 0
        for i in range(len(s)):
            if i > 0 and lookup[s[i]] > lookup[s[i-1]]:
                print(res)
                print(lookup[s[i]])
                res = res + lookup[s[i]] - 2 * lookup[s[i-1]]
            else:
                res += lookup[s[i]]
        return res

solution = Solution()
a = solution.romanToInt("IV")
print(a)