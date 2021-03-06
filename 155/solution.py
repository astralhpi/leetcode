class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        else:
            self.min.append(
                min(self.min[-1], x))
        

    def pop(self):
        """
        :rtype: void
        """
        result = self.data[-1]
        del self.data[-1]
        del self.min[-1]
        return result
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
