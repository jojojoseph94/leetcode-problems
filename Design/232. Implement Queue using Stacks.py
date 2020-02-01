"""
Queue using 2 stacks
insert operation - just insert to top of in_stack
pop operation - If out_stack is not empty, pop the element in top of out_stack.
                If not, pop every element in in_stack and append to out_stack, then pop element at top of 
                out_stack
peek - Same as pop, just dont remove the element from the out_stack.

Space complexity -> O(n)
Time complexity -> push - O(1)
                   pop - Worst case -> O(n), Best case O(1), Average -> O(1)
                   peek - Worst case -> O(n), Best case O(1), Average -> O(1)

"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # push to instack
        self.in_stack.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # check if outstack is empty
        if self.out_stack:
            return self.out_stack.pop(-1)
        else:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop(-1))
            return self.out_stack.pop(-1)
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.out_stack:
            return self.out_stack[-1]
        elif self.in_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop(-1))
            return self.out_stack[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.in_stack == [] and self.out_stack == []:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()