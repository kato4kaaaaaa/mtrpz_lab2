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

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        new_node = Node(element)
        if self.tail is None:  # Порожній список
            if index != 0:
                raise IndexError("Index out of bounds")
            new_node.next = new_node
            self.tail = new_node
        elif index == 0:  # Вставка в голову
            new_node.next = self.tail.next
            self.tail.next = new_node
        else:
            current = self.tail.next  # Починаємо з голови
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if index == self._size:  # Вставка в кінець
                self.tail = new_node
        self._size += 1
