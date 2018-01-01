class MultiStack:

    def __init__(self, numStacks):
        self.numStacks = numStacks

        #the actual stacks themselves
        self.stacks = []
        #heads for each stack. stack 0 in index 0 etc...
        self.heads = []
        for index in range(0, numStacks):
            heads.append(index)

    def push(self, stackid, data):
        if stackid >= self.numStacks:
            print("stack out of bounds")
            return
        if self.heads[stackid] < self.numStacks:
            self.stacks[self.heads[stackid]] = data
        else:
            self.heads[stackid] += numStacks
            self.stacks[self.heads[stackid]] = data

    def pop(self, stackid):
        if stackid >= self.numStacks:
            print("stack out of bounds")
            return
        try:
            returning = self.stacks[self.heads[stackid]]
        except IndexError:
            print("out of bounds")
            return
        self.stacks[self.heads[stackid]] = 0
        if self.heads[stackid] > self.numStacks:
            self.heads[stackid] -= self.numStacks
        return returning
