def huiwen(x):
    if x < 0 or (int(str(x)[-1])) == 0 :
        return False
    else:
        return True
print(huiwen(990))















"--------------------------answer--------------------------"
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x != int(str(x)[::-1]):
            return False
        else:
            return True