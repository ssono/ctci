class Queue:

    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        return self.items == []

    def enqueue(self, data):
        self.size += 1
        self.items.insert(0, data)

    def dequeue(self):
        if(self.size > 0):
            self.size -= 1
            return self.items.pop()
        return None

    def size(self):
        return self.size
