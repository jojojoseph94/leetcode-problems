"""
Soln : stack to store numbers, keep track of last_number and last_symbol
       Initialize with + and 0.
       When a number process it to last_number
       When a symbol comes, remove num from stack, operate with last_number and push to stack
       Finally just add the numbers on the stack

Time complexity : O(N)
Space complexity : O(N) -> for stack
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        number_stack = []
        last_symbol = "+"
        last_number = 0
        for i in s:
            if i == " ":
                continue
            if i in ["+","-","/","*"]:
                if last_symbol == "*":
                    num = number_stack.pop(-1)
                    num*=last_number
                    number_stack.append(num)
                elif last_symbol == "/":
                    num = number_stack.pop(-1)
                    if num//last_number <0 and num%last_number!=0:
                        num=num//last_number+1
                    else:
                        num//=last_number
                    number_stack.append(num)
                elif last_symbol == "-":
                    number_stack.append(-last_number)
                else:
                    number_stack.append(last_number)
                last_symbol = i
                last_number = 0
            else:
                last_number = last_number*10 + int(i)
        print number_stack, last_number, last_symbol
        if last_symbol == "*":
            num = number_stack.pop(-1)
            num*=last_number
            number_stack.append(num)
        elif last_symbol == "/":
            num = number_stack.pop(-1)
            if num//last_number <0 and num%last_number!=0:
                num=num//last_number+1
            else:
                num//=last_number
            number_stack.append(num)
        elif last_symbol == "-":
            number_stack.append(-last_number)
        else:
            number_stack.append(last_number)
        last_number = 0
        for i in number_stack:
            last_number+=i
        return last_number