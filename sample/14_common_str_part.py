def common(ll):
    for i in range(len(ll[0])):
        for j in ll:
            if len(j) <= i or ll[0][i] != j[i]:
                return ll[0][:i]
    return ll[0]

a = common(["aab", "aaoq", "aalp"])
print(a)





















"--------------------answer----------------------"
import os


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return os.path.commonprefix(strs)

# solution = Solution()
# print(solution.longestCommonPrefix(["abfsaf", "abywrw", "abqrewr"]))