class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class linkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    #adds to the front
    def add(self, newdata):
        newhead = Node(newdata)
        newhead.setNext(self.head)
        self.head = newhead

    def __str__(self):
        current = self.head
        string = ""
        while(current != None):
            string += str(current.getData()) + " "
            current = current.getNext()
        return string

class orderedLinkedList(linkedList):

    #recursively find spot for new node, then insert
    def add(self, newdata):
        if(self.head == None):
            newhead = Node(newdata)
            self.head = newhead
            return

        head = self.head
        prev = None

        while(newdata > head.getData()):
                prev = head
                head = head.getNext()

        newnode = Node(newdata)
        newnode.setNext(head)
        if(prev != None):
            prev.setNext(newnode)
        if(head == self.head):
            self.head = newnode
