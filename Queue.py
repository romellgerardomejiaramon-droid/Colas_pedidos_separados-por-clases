from Node import Node
from Order import Order
from QueueInterface import QueueInterface


class Queue(QueueInterface):

    def __init__(self):
        self.top = None
        self.tail = None

    def size(self):
        count = 0
        current = self.top
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def isEmpty(self):
        return self.top is None

    def front(self):
        if self.isEmpty():
            return None
        return self.top.getInfo()

    def enqueue(self, info):
        newNode = Node(info)
        if self.isEmpty():
            self.top = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return None
        item = self.top.getInfo()
        self.top = self.top.getNext()
        if self.top is None:
            self.tail = None
        return item

    def printInfo(self):
        print("********* QUEUE DUMP *********")
        print("   Size: " + str(self.size()))
        node = self.top
        elementIndex = 1
        while node is not None:
            print("   ** Element " + str(elementIndex))
            info = node.getInfo()
            if isinstance(info, Order):
                info.print()
            else:
                print("     Info: " + str(info))
            node = node.getNext()
            elementIndex += 1
        print("******************************")

    def getNth(self, pos):
        if pos < 1:
            return None
        current = self.top
        currentPos = 1
        while current is not None:
            if currentPos == pos:
                return current.getInfo()
            current = current.getNext()
            currentPos += 1
        return None
