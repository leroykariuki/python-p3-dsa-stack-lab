class Stack:
    def __init__(self, limit=None):
        if isinstance(limit, list):
            self.items = list(limit)
            self.limit = None  # No limit for list initialization
        else:
            self.items = []
            self.limit = limit

    def push(self, item):
        if self.limit is None or len(self.items) < int(self.limit):
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return self.limit is not None and len(self.items) == self.limit

    def search(self, value):
        try:
            index = self.items.index(value)
            return len(self.items) - index
        except ValueError:
            return -1
