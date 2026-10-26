import time
from Order import Order
from Queue import Queue


class TestQueue:

    @staticmethod
    def main():
        start_time = time.time()

        cola = Queue()

        p1 = Order(20, "cust1")
        p2 = Order(30, "cust2")
        p3 = Order(40, "cust3")
        p4 = Order(50, "cust3")

        cola.enqueue(p1)
        cola.enqueue(p2)
        cola.enqueue(p3)
        cola.enqueue(p4)

        cola.printInfo()

        f = cola.front()
        if isinstance(f, Order):
            f.print()

        n3 = cola.getNth(3)
        if isinstance(n3, Order):
            n3.print()

        d = cola.dequeue()
        if isinstance(d, Order):
            d.print()

        cola.printInfo()

        end_time = time.time()
        duration_ms = (end_time - start_time) * 1000
        print(f"\nTiempo de ejecucion: {duration_ms:.4f} ms")


if __name__ == "__main__":
    TestQueue.main()
