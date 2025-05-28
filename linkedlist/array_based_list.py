class ArrayBasedList:
    def __init__(self):
        self.data = []

    def length(self) -> int:
        return len(self.data)

    def append(self, element: str) -> None:
        self.data.append(element)

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of bounds")
        self.data.insert(index, element)

    def delete(self, index: int) -> str:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data.pop(index)

    def deleteAll(self, element: str) -> None:
        self.data = [x for x in self.data if x != element]

    def get(self, index: int) -> str:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data[index]

    def clone(self) -> 'ArrayBasedList':
        new_list = ArrayBasedList()
        new_list.data = self.data.copy()
        return new_list

    def reverse(self) -> None:
        self.data.reverse()



