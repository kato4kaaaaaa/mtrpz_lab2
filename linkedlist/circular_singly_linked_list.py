class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.tail = None
        self._size = 0

    def length(self):
        return self._size

    def append(self, element: str):
        new_node = Node(element)
        if self.tail is None:
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
