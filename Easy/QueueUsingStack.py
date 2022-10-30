class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        while self.inStack:
            self.outStack.append(self.inStack.pop())
        self.inStack.append(x)
        while self.outStack:
            self.inStack.append(self.outStack.pop())

    def pop(self) -> int:
        return self.inStack.pop()

    def peek(self) -> int:
        return self.inStack[-1]

    def empty(self) -> bool:
        return not self.inStack and not self.outStack 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
