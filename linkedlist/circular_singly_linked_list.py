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

    def deleteAll(self, element: str) -> None:
        if self.tail is None:
            return

        current = self.tail.next
        prev = self.tail
        count = self._size

        i = 0
        while i < count:
            if current.data == element:
                # Видаляємо current
                if current == self.tail:
                    if self._size == 1:
                        self.tail = None
                        self._size -= 1
                        break
                    else:
                        prev.next = current.next
                        self.tail = prev
                        current = current.next
                        self._size -= 1
                else:
                    prev.next = current.next
                    current = current.next
                    self._size -= 1
                count -= 1  # зменшуємо ітерацію, бо список став коротшим
                # i не збільшуємо, бо current змінився
            else:
                prev = current
                current = current.next
                i += 1

    def get(self, index: int) -> str:
        if index < 0 or index >= self._size or self.tail is None:
            raise IndexError("Index out of bounds")

        current = self.tail.next
        for _ in range(index):
            current = current.next
        return current.data

    def clone(self) -> 'CircularSinglyLinkedList':
        new_list = CircularSinglyLinkedList()
        if self.tail is None:
            return new_list  # Порожній список

        current = self.tail.next
        for _ in range(self._size):
            new_list.append(current.data)
            current = current.next
        return new_list

