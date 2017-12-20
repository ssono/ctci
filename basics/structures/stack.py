class Stack:

    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        return self.items == []

    def push(self, data):
        self.size += 1
        self.items.append(data)

    def pop(self):
        if(self.size > 0):
            self.size -= 1
            return self.items.pop()
        return None

    def peek(self):
        return self.items[self.size - 1]

    def size(self):
        return self.size
