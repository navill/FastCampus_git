class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n


class LQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def empty(self):
        if self.front is None:
            return True
        else:
            return False

    def enqueue(self, data):
        new_node = Node(data)
        new_node.next = self.rear


    def dequeue(self):
        pass

    def peek(self):
        if self.empty():
            return

        return self.front.data


if __name__ == '__main__':
    q = LQueue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    while not q.empty():
        print(q.dequeue())
