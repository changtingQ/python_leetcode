# def add_binary(str_1: str, str_2: str):
#     if len(str_1) > len(str_2):
#         max_len = len(str_1)
#     else:
#         max_len = len(str_2)
#     str_1 = ""
#     for i in range(max_len - 1, -1, -1):
#         if str_1[i] + str_2[i] == 2:
#             str_1 += "0"
#             str_1 += "1"


# result = add_binary("11", "11")
# print(result)

"-----------------------answer----------------------思路1"
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

# solution = Solution()
# result = solution.addBinary("11", "1")
# print(result)

"-------------------answer----------------------思路2"

class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if (a == '' or b == ''):
            return a + b
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        elif a[-1] == '1' and b[-1] == '1':
            return self.addBinary(a[:-1], self.addBinary(b[:-1],'1')) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'

solution = Solution()
result = solution.addBinary("10", "10")
print(result)

