class TreeNode:

    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getKey(self):
        return self.key

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def setData(self, newdata):
        self.data = newdata

    def setLeft(self, newleft):
        self.left = newleft

    def setRight(self, newright):
        self.right = newright

    def setParent(self, newparent):
        self.parent = newparent

    def hasLeft(self):
        if self.left != None:
            return True
        return False

    def hasRight(self):
        if self.right != None:
            return True
        return False

    def hasBoth(self):
        if self.left != None and self.right != None:
            return True
        return False

    def hasAny(self):
        if self.left != None or self.right != None:
            return True
        return False


class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return self.size

    def size(self):
        return self.size

    #find appropriate spot by searching for the node that isnt there, place the new node
    def add(self, key, data):
        newnode = TreeNode(key, data)
        current = self.root
        if(current == None):
            self.root = newnode
            return
        while(True):
            if(newnode.getKey() > current.getKey()):
                if(current.hasRight()):
                    current = current.getRight()
                    continue
                else:
                    current.setRight(newnode)
                    newnode.setParent(current)
                    self.size += 1
                    break
            else:
                if(current.hasLeft()):
                    current = current.getLeft()
                    continue
                else:
                    current.setLeft(newnode)
                    newnode.setParent(current)
                    self.size += 1
                    break

    #search using BST conventions left when desired < current, right when desired > current
    def search(self, key):
        current = self.root
        if(current == None):
            return None
        while(current.hasAny() or current == self.root):
            if(current.getKey() == key):
                return current
            elif(key > current.getKey()):
                current = current.getRight()
            else:
                current = current.getLeft()
        return current

    #find the node to be removed,
    def remove(self, key):
        removed = self.search(key)
        if(removed == None):
            return removed
        #if removed is root: root = right,
        if(removed == self.root):
            newroot = self.root.getRight()
            self.root = newroot
            if(newroot != None):
                newroot.setParent(None)
                while(newroot.hasLeft()):
                    newroot = newroot.getLeft()
                newroot.setLeft(removed.getLeft())
                if(newroot.getLeft() != None):
                    newroot.getLeft().setParent(newroot)
            return removed

        if(not removed.hasAny()):
            parent = removed.getParent()
            if(parent.getLeft() == removed):
                parent.setLeft(None)
            else:
                parent.setRight(None)
            return removed


        elif(removed.hasBoth() or removed.hasRight()):
            new = removed.getRight()
            new.setParent(removed.getParent())
            parent = new.getParent()
            if(parent.getLeft() == removed):
                parent.setLeft(new)
            else:
                parent.setRight(new)
            while(new.hasLeft()):
                new = new.getLeft()
            new.setLeft(removed.getLeft())
            return removed

        else:
            new = removed.getLeft()
            new.setParent(removed.getParent())
            parent = new.getParent()
            if(parent.getLeft() == removed):
                parent.setLeft(new)
            else:
                parent.setRight(new)
            return removed
