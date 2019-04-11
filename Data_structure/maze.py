from lstack import LStack


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self):
        if not self.head:
            return True
        return False

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

