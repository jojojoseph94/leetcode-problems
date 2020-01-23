"""
Decode String : Using 2 stacks, one for number stack and one for string stack
                if num, add to num (build num using num =  num*10 + i)
                if character, add to current character array
                if open braces, push both number and cur string to respective stacks and reset them
                if closin braces, pop number from num stack, multiply with cur string
                and then pop from str stack and add that to front of cur string
Time complexity : O(N) Linear -> Each character is visited only once
Space complexity : O(N) Max all chars in stack ??
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cur_num = 0
        cur_str = ""
        num_stack = []
        str_stack = []
        for i in s:
            print cur_num, cur_str, num_stack, str_stack
            try:
                i = int(i)
                cur_num = cur_num*10 + int(i)
            except ValueError:
                if i.isalpha():
                    cur_str+=i
            if i == '[':
                num_stack.append(cur_num)
                cur_num = 0
                str_stack.append(cur_str)
                cur_str = ""
            if i == ']':
                nm = num_stack.pop(-1)
                cur_str*=nm
                cur_str = str_stack.pop(-1) + cur_str
        return cur_str
        