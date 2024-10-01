class MinStack:

    def __init__(self):
        self.Stack = []
        self.ministack = []

    def push(self, val: int) -> None:
        self.Stack.append(val)
        if self.ministack:
            self.ministack.append(min(self.ministack[-1], val))
        else:
            self.ministack.append(val)

    def pop(self) -> None:
        self.Stack.pop()
        self.ministack.pop()

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.ministack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
