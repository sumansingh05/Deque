class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)==0
    
    def insertFront(self,data):
        self.items.insert(0,data)

    def insertRear(self,data):
        self.items.append(data)
    
    def deleteFront(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.items.pop(0)

    def deleteRear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.items.pop()

    def getFront(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
             return self.items[0]
        
    def getRear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
             return self.items[-1]
        
    def size(self):
        return len(self.items)
    
d1 = Deque()
d1.insertFront(10)
d1.insertFront(20)
d1.insertRear(30)
d1.insertRear(40)
print(d1.getFront(),d1.getRear())


