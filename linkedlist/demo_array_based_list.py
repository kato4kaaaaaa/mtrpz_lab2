from array_based_list import ArrayBasedList


def demo():
    print("Створення списку...")
    lst = ArrayBasedList()

    print("Додаємо елементи: a, b, c")
    lst.append('a')
    lst.append('b')
    lst.append('c')
    print("Після append:", lst.data)

    print("Вставляємо 'z' на початок, 'y' на позицію 2, 'x' в кінець")
    lst.insert('z', 0)
    lst.insert('y', 2)
    lst.insert('x', lst.length())
    print("Після insert:", lst.data)

    print("Видаляємо елемент на позиції 2:", lst.delete(2))
    print("Після delete:", lst.data)

    print("Додаємо кілька 'a' для deleteAll")
    lst.append('a')
    lst.append('a')
    print("Перед deleteAll('a'):", lst.data)
    lst.deleteAll('a')
    print("Після deleteAll('a'):", lst.data)

    print("Отримуємо елемент на позиції 1:", lst.get(1))

    print("Клонуємо список...")
    clone_lst = lst.clone()
    print("Клон списку:", clone_lst.data)

    print("Перевертаємо список...")
    lst.reverse()
    print("Після reverse:", lst.data)

    print("Пошук першого входження 'y':", lst.findFirst('y'))
    print("Пошук останнього входження 'y':", lst.findLast('y'))

    print("Очищаємо список...")
    lst.clear()
    print("Після clear, довжина:", lst.length())

    print("Розширюємо список елементами клону")
    lst.extend(clone_lst)
    print("Після extend:", lst.data)


if __name__ == "__main__":
    demo()
