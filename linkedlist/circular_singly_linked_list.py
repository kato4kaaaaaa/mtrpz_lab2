class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.tail = None
        self._size = 0

    def length(self) -> int:
        return self._size

    def append(self, element: str) -> None:
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

    def reverse(self) -> None:
        if self.tail is None or self._size == 1:
            return  # Порожній або один елемент — нічого міняти

        prev = self.tail
        current = self.tail.next
        old_head = current  # Зберігаємо стару голову

        for _ in range(self._size):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.tail = old_head  # Старий голова стає новим хвостом

    def findFirst(self, element: str) -> int:
        if self.tail is None:
            return -1
        current = self.tail.next
        for i in range(self._size):
            if current.data == element:
                return i
            current = current.next
        return -1

    def findLast(self, element: str) -> int:
        if self.tail is None:
            return -1
        current = self.tail.next
        last_pos = -1
        for i in range(self._size):
            if current.data == element:
                last_pos = i
            current = current.next
        return last_pos

    def clear(self) -> None:
        self.tail = None
        self._size = 0

    def extend(self, elements: 'CircularSinglyLinkedList') -> None:
        if elements.tail is None:
            return  # Якщо другий список пустий, нічого не робимо

        current = elements.tail.next
        for _ in range(elements._size):
            self.append(current.data)
            current = current.next


def demo():
    print("Створення списку...")
    csll = CircularSinglyLinkedList()

    # append
    csll.append('a')
    csll.append('b')
    csll.append('c')
    print(f"Після append: {[csll.get(i) for i in range(csll.length())]}")

    # insert
    csll.insert('z', 0)  # вставити на початок
    csll.insert('y', 2)  # вставити в середину
    csll.insert('x', csll.length())  # вставити в кінець
    print(f"Після insert: {[csll.get(i) for i in range(csll.length())]}")

    # delete
    deleted = csll.delete(2)
    print(f"Видалено елемент на позиції 2: {deleted}")
    print(f"Після delete: {[csll.get(i) for i in range(csll.length())]}")

    # deleteAll
    csll.append('a')
    csll.append('a')
    print(f"Перед deleteAll('a'): {[csll.get(i) for i in range(csll.length())]}")
    csll.deleteAll('a')
    print(f"Після deleteAll('a'): {[csll.get(i) for i in range(csll.length())]}")

    # get
    print(f"Елемент на позиції 1: {csll.get(1)}")

    # clone
    cloned = csll.clone()
    print(f"Клон списку: {[cloned.get(i) for i in range(cloned.length())]}")

    # reverse
    csll.reverse()
    print(f"Після reverse: {[csll.get(i) for i in range(csll.length())]}")

    # findFirst & findLast
    csll.append('y')
    print(f"findFirst('y'): {csll.findFirst('y')}")
    print(f"findLast('y'): {csll.findLast('y')}")

    # clear
    csll.clear()
    print(f"Після clear, довжина: {csll.length()}")

    # extend
    list1 = CircularSinglyLinkedList()
    list2 = CircularSinglyLinkedList()
    for ch in ['p', 'q', 'r']:
        list1.append(ch)
    for ch in ['x', 'y']:
        list2.append(ch)
    list1.extend(list2)
    print(f"Після extend: {[list1.get(i) for i in range(list1.length())]}")

if __name__ == "__main__":
    demo()
