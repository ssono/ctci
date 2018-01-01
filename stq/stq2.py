import math
class minStack:

    def __init__(self):
        self.items[]
        self.head = 0
        self.min = math.inf

    def push(self, data):
        if data < self.min:
            self.min = data
        if len(self.items) > 0:
            self.head += 1
        self.items.append(data)

    def pop(self):
        if len(self.items) > 0:
            returning = self.items[self.head]
            self.items[self.head] = 0
            del self.items[self.head]
            self.head -= 0

            if returning == self.min:
                self.min = min(self.items)

    def getMin(self):
        return self.min
