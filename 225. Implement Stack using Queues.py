class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.internalQueue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        return self.internalQueue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int

        """
        return self.internalQueue.pop(-1)


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.internalQueue[-1]

    def size(self):
        return len(self.internalQueue)

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return True if len(self.internalQueue) == 0 else False


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.internalStackMain = MyStack()
        self.internalStackTemp = MyStack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.internalStackMain.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.internalStackMain.size() > 1:
            self.internalStackTemp.push(self.internalStackMain.pop())

        popResult = self.internalStackMain.pop()

        while not self.internalStackTemp.empty():
            self.internalStackMain.push(self.internalStackTemp.pop())

        return popResult


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.internalStackMain.size() > 1:
            self.internalStackTemp.push(self.internalStackMain.pop())

        peekResult = self.internalStackMain.pop()
        self.internalStackMain.push(peekResult)

        while not self.internalStackTemp.empty():
            self.internalStackMain.push(self.internalStackTemp.pop())

        return peekResult


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.internalStackMain.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()