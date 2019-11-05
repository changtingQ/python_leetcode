def str_word_max_lenth(str_1: str):
    str_1 = str_1.strip(" ")
    str_list = str_1.split()
    back_len = len(str_list[-1])
    return back_len


result = str_word_max_lenth("hello world")
print(result)















"------------------------answer---------------------------"
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])