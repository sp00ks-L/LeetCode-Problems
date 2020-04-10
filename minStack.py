from collections import deque


class MinStack:
    '''
    Design a stack that supports push, pop, top and get_min in constant time
    '''

    def __init__(self):
        """
        Initialise data structure
        Originally had stack=deque() as default arg but it threw wrong answers during submission
        """
        self.stack = deque()

    def __del__(self):
        print("Destructor called, Stack deleted")

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> None:
        self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return min(self.stack)

