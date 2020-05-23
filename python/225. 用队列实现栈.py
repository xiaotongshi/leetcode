class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        x = self.stack[-1]
        del self.stack[-1]
        return x


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.stack:
            return False
        else:
            return True



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()