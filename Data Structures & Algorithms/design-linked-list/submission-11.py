class MyLinkedList:

    def __init__(self):
        self = self
        self.head = None
        self.tail = None
        self.size = 0

    class Node:
        def __init__(self, value = 0, previous = None, nex = None):
            self = self
            self.value = value
            self.previous = previous
            self.nex = nex

    def get(self, index: int) -> int:
        if self.head == None or self.size == 0 or index < 0 or index >= self.size:
            return -1
        node = self.head
        i = 0
        while (i < index):
            node = node.nex
            i += 1
        return node.value

    def addAtHead(self, val: int) -> None:
        new_node = self.Node(val, None, self.head)
        self.head = new_node
        self.size += 1
        if self.head.nex != None:
            self.head.nex.previous = self.head
        if self.size == 1:
            self.tail = self.head
        return None

    def addAtTail(self, val: int) -> None:
        if self.tail == None:
            self.head = self.Node(val, None, None)
            self.tail = self.head
        else:
            node = self.tail
            node.nex = self.Node(val, node, None)
            self.tail = node.nex
        self.size += 1
        return None
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return -1
        elif index == 0 or self.size == 0:
            self.addAtHead(val)
            return None
        elif index == self.size:
            self.addAtTail(val)
            return None
        
        i = 0
        node = self.head
        while (i < index - 1):
            node = node.nex
            i += 1
        new_node = self.Node(val, node, node.nex)
        node.nex.previous = new_node
        node.nex = new_node
        self.size += 1
        return None

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1
        elif index == 0:
            if self.size == 1:
                self.size -= 1
                self.head = None
                self.tail = None
                return None
            else:
                self.head = self.head.nex
                self.head.previous = None
                self.size -= 1
                return None
        elif index == self.size - 1:
            self.tail = self.tail.previous
            self.tail.nex = None
            self.size -= 1
            return None

        i = 0
        node = self.head
        while (i < index - 1):
            node = node.nex
            i += 1
        node.nex = node.nex.nex
        node.nex.previous = node
        self.size -= 1
        return None

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)