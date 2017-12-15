class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

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

    def __str__(self):
        current = self.head
        string = ""
        while(current != None):
            string += str(current.getData()) + " "
            current = current.getNext()
        return string

    #returns true if empty
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

    #returns the size of the linkedList
    def size(self):
        head = self.head
        count = 0
        while(head != None):
            count += 1
            head = head.getNext()
        return count

    #returns first node of desired value and None if it doesn't exist
    def search(self, value):
        head = self.head
        node = None
        while(head != None):
            if(head.getData() == value):
                node = head
                break
            head = head.getNext()
        return node

    #removes first node of desired value and deletes it
    def remove(self, value):
        head = self.head
        prev = None
        node = None
        while(head != None):
            if(head.getData() == value):
                node = head
                if(node == self.head):
                    self.head = node.getNext()
                else:
                    prev.setNext(node.getNext())
                break

            prev = head
            head = head.getNext()
        return node



class orderedLinkedList(linkedList):

    #find spot for new node, then insert
    def add(self, newdata):
        #if empty set as head
        if(self.head == None):
            newhead = Node(newdata)
            self.head = newhead
            return

        head = self.head
        prev = None

        #find first elem >= newdata
        while(head != None and newdata > head.getData()):
                prev = head
                head = head.getNext()

        #insert node and connect around
        newnode = Node(newdata)
        newnode.setNext(head)
        if(prev != None):
            prev.setNext(newnode)
        if(head == self.head):
            self.head = newnode
