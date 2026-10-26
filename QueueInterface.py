from abc import ABC, abstractmethod


class QueueInterface(ABC):

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def front(self):
        pass

    @abstractmethod
    def enqueue(self, info):
        pass

    @abstractmethod
    def dequeue(self):
        pass
