class Node:

    def __init__(self, info):
        self.info = info
        self.next = None

    def getInfo(self):
        return self.info

    def setInfo(self, info):
        self.info = info

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next
