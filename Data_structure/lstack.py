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


class lstack:
    def __init__(self):
        self.top = None

    def empty(self):
        pass

    def push(self, data):
        return

    def pop(self):
        return

    def peek(self):
        return


