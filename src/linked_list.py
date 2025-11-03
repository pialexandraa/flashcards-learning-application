from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next



