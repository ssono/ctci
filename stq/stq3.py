"""implement setOfStacks so that when the capacity of the first stack is filled,
 it will overflow into the next stacks.
 supports push pop"""

class setOfStacks:

    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity
        #head: self.stacks[self.size // self.capacity][self.size % self.capacity]
        self.size = 0

    def __str__(self):
        string = ""
        for l in self.stacks:
            for item in l:
                string += str(item) + " "
            string += "\n"
        return string

    def push(self, data):
        if self.size % self.capacity == 0:
            self.stacks.append([])
        self.stacks[self.size // self.capacity].append(data)
        self.size += 1

    def pop(self):
        if self.size <= 0:
            return
        self.size -= 1
        returning = self.stacks[self.size // self.capacity][self.size % self.capacity]
        if self.size % self.capacity == 0:
            del self.stacks[self.size // self.capacity]
        return returning

s = setOfStacks(3)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
print(s)
for i in range(4):
    print(s.pop())
