class MinStack:

    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, val: int, nex, mini: int):
            self.val = val
            self.nex = nex
            if val < mini:
                self.mini = val
            else:
                self.mini = mini
        

    def push(self, val: int) -> None:
        if self.head == None:
            node = self.Node(val, None, val)
            self.head = node
        else:
            node = self.Node(val, self.head, self.head.mini)
            self.head = node
        return None

    def pop(self) -> None:
        self.head = self.head.nex
        return None
        

    def top(self) -> int:
        return self.head.val
        

    def getMin(self) -> int:
        return self.head.mini
        
