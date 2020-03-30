"""
Logic : use a stack to push symbol and number at each occurance of "("
        When ")", "+", or "-" occurrs, process the expression

Time complexity : O(N) -> Each element is visited once
Space complexity : O(N) -> Stack can be max size n/2
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0
        num = 0
        sign = 1
        for i in s:
            #print stack,ans, num, sign
            if i.isdigit():
                num = num*10 + int(i)
            elif i == "(":
                #push current result to stack
                stack.append(ans)
                stack.append(sign)
                # reset stuff
                ans = 0
                sign = 1
            elif i == " ":
                continue
            elif i == ")":
                ans += (sign*num)
                ans *= stack.pop(-1)
                ans += stack.pop(-1)
                num = 0
            elif i == "-":
                ans = ans + (sign * num)
                num = 0
                sign = -1
            else:
                ans = ans + (sign * num)
                num = 0
                sign = 1
        return ans + sign*num