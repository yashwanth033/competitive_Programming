class Stack():
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):
    # Implement the push, pop, and get_max methods
    def __init__(self):
        self.mainStack = Stack()
        self.MaxStack = Stack()

    def push(self, item):
        if self.MaxStack.peek()>item:
            self.MaxStack.push(self.MaxStack.peek())
        else:
            self.MaxStack.push(item)
        self.mainStack.push(item)

    def pop(self):
        x = self.mainStack.pop()
        self.MaxStack.pop()
        return x

    def get_max(self):
        return self.MaxStack.peek()
