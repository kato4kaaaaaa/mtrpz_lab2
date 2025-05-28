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

        if self.tail is None:
            if index != 0:
                raise IndexError("Index out of bounds")
            new_node.next = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.tail.next
            self.tail.next = new_node
        else:
            current = self.tail.next
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if index == self._size:
                self.tail = new_node

        self._size += 1

    def delete(self, index: int) -> str:
        if self.tail is None or index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        prev = self.tail
        current = self.tail.next  # Починаємо з голови

        for _ in range(index):
            prev = current
            current = current.next

        # Видаляємо current
        if current == self.tail:
            if self._size == 1:
                self.tail = None
            else:
                prev.next = current.next
                self.tail = prev
        else:
            prev.next = current.next

        self._size -= 1
        return current.data
