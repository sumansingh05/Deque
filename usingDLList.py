class Node:
    def __init__(self,data):
        self.item = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.front is None
    
    def insertFront(self,data):
        newNode = Node(data)
        if self.is_empty():            
            self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
        self.front = newNode
        self.count += 1

    def insertRear(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.front = newNode            
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
        self.rear = newNode 
        self.count += 1

    def deleteFront(self):
        if self.is_empty():
            raise IndexError("list is empty")
            return
        else:
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
                self.front.prev = None
            self.count -= 1

    def deleteRear(self):
        if self.is_empty():
            raise IndexError("list is empty")
            return
        else:
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next = None
            self.count -= 1

    def getFront(self):
        if self.is_empty():
            raise IndexError("list is empty")            
        else:
            return self.front.item
        
    def getRear(self):
        if self.is_empty():
            raise IndexError("list is empty")           
        else:
            return self.rear.item
        
    def display(self):
        if self.is_empty():
            raise IndexError("list is empty")
        else:
            current = self.front
            print("Deque is: ",end=" ")
            while current:
                print(current.item,end=" ")
                current = current.next
            print()


        
d1 = Deque()
print(d1.is_empty())
d1.insertFront(2)
d1.insertFront(1)
d1.insertRear(3)
d1.insertRear(4)
d1.display()
print("Size of Deque is ",d1.count)
print("Front data is ",d1.getFront())
print("Rear data is ",d1.getRear())
d1.deleteFront()
d1.display()
print("Size of Deque is ",d1.count)
print("Front data is ",d1.getFront())
print("Rear data is ",d1.getRear())




