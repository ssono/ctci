"""queue via stacks:
define a queue using only 2 stacks"""


class Staq:

    def __init__(self):
        self.input = []
        self.out = []

    def enqueue(self, data):
        self.input.append(data)

    def deque(self):
        if len(self.out) > 0:
            return self.out.pop()
        while len(self.input) > 0:
            self.out.append(self.input.pop())
        return self.out.pop()

t = Staq()
for i in range(5):
    t.enqueue(i)
print(str(t.deque()))
print(str(t.deque()))
print(str(t.deque()))
for i in range(5, 8):
    t.enqueue(i)
for i in range(5):
    print(str(t.deque()))
