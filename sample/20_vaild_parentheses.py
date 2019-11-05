def plp_matach(x):
    LEFT = {'(', '[', '{'}  # 左括号
    RIGHT = {')', ']', '}'}  # 右括号
    stack = []  # 创建一个栈
    for i in x:
        if i in LEFT:
            stack.append(x)
        elif i in RIGHT:
            if not stack or not 1 <= ord(i)- ord(stack[-1]) <= 2 :
                return False
            stack.pop()
    return not stack



























"--------------------answer----------------------"


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        LEFT = {'(', '[', '{'}  # 左括号
        RIGHT = {')', ']', '}'}  # 右括号
        stack = []  # 创建一个栈
        for brackets in s:  # 迭代传过来的所有字符串
            if brackets in LEFT:  # 如果当前字符在左括号内
                stack.append(brackets)  # 把当前左括号入栈
            elif brackets in RIGHT:  # 如果是右括号
                if not stack or not 1 <= ord(brackets) - ord(stack[-1]) <= 2:
                    # 如果当前栈为空，()]
                    # 如果右括号减去左括号的值不是小于等于2大于等于1
                    return False  # 返回False
                stack.pop()  # 删除左括号
        return not stack  # 如果栈内没有值则返回True，否则返回False


# s = Solution()
# print(s.isValid("([[])[]{}"))
# print(s.isValid("([])[]{}"))
