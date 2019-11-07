import math
("X")
def climb_jie(n: int):
    if n % 2 == 0:
        num_int = math.ceil(n / 2)
        print(num_int)
        a = 0
        for i in range(num_int+1, n):
            a += i
        # print(a)
        a += 2
    else:
        num_int = math.ceil(n / 2)
        print(num_int)
        a = 0
        for i in range(num_int, n):
            a += i
        # print(a)
        a += 1
    return a


result = climb_jie(n=6)         # n = 6 |  111111, 11112, 11121, 11211, 12111, 21111, 1122, 1221, 2211, 2112, 1212, 2121, 222
print(result)                   # n = 5 |  11111, 1112, 1121, 1211, 2111, 122, 212, 221,
                                # n = 4 |  1111, 112, 121, 211, 22
                                # n = 3 |  111, 12, 21
                                # n = 2 |  11, 2
                                # n = 1 |  1



print("*****************answer******************思路1")

# python3 斐波那契数列
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

solution = Solution()
result = solution.climbStairs(n=6)
print(result)







print("*****************answer******************思路2")