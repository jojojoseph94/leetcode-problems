"""
Algorithm - Single stack
We use one stack only and a variable to store min element.
If the element to be inserted is less than or equal to(equal to because duplicate elements which can be same min) min element, then we push the current min element to stack, then
update the min element to new element and then push new element to stack.
If it isn't then simply push that element to stack

While popping an element, check the element is same as min, If it is, pop the element, then pop once more to retrieve
the previous minimum element as well.

Time Complexity
1. To add an element - O(1)
2. To retrieve top element - O(1)
3. To get min element - O(1)

Space complexity 
1. O(n) - Worst case would be elements added in descending order which would result in 2n elements in stack

NOTE - This can also be done with 2 stacks (one regular stack and one minimum stack) but the complexities remain same.

"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min == None:
            self.min = x
        elif x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.min == self.stack[-1]:
            self.stack.pop(-1)
            try:
                self.min = self.stack[-1]
                self.stack.pop(-1)
            except IndexError:
                self.min = None
        else:
            self.stack.pop(-1)       

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()