from .circular_list import CircularSinglyLinkedList


def test_append_and_length():
    lst = CircularSinglyLinkedList()
    assert lst.length() == 0
    lst.append('a')
    lst.append('b')
    assert lst.length() == 2
    assert lst.get(0) == 'a'
    assert lst.get(1) == 'b'

def test_insert_and_get():
    lst = CircularSinglyLinkedList()
    lst.append('a')
    lst.append('c')
    lst.insert('b', 1)
    assert lst.get(1) == 'b'
    assert lst.length() == 3
def test_insert_invalid_index():
    lst = CircularSinglyLinkedList()
    with pytest.raises(IndexError):
        lst.insert('x', -1)
    with pytest.raises(IndexError):
        lst.insert('x', 1)

def test_get_invalid_index():
    lst = CircularSinglyLinkedList()
    with pytest.raises(IndexError):
        lst.get(0)
    lst.append('a')
    with pytest.raises(IndexError):
        lst.get(1)

def test_delete_invalid_index():
    lst = CircularSinglyLinkedList()
    with pytest.raises(IndexError):
        lst.delete(0)
    lst.append('a')
    with pytest.raises(IndexError):
        lst.delete(1)
def test_delete():
    lst = CircularSinglyLinkedList()
    lst.append('a')
    lst.append('b')
    deleted = lst.delete(0)
    assert deleted == 'a'
    assert lst.length() == 1

def test_deleteAll():
    lst = CircularSinglyLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('a')
    lst.deleteAll('a')
    assert lst.length() == 1
    assert lst.get(0) == 'b'
def test_clone():
    lst = CircularSinglyLinkedList()
    lst.append('a')
    clone = lst.clone()
    assert clone.length() == lst.length()
    assert clone.get(0) == 'a'
    clone.append('b')
    assert lst.length() == 1  # оригінал не змінився

def test_reverse():
    lst = CircularSinglyLinkedList()
    for ch in ['a', 'b', 'c']:
        lst.append(ch)
    lst.reverse()
    assert lst.get(0) == 'c'
    assert lst.get(2) == 'a'

def test_findFirst_and_findLast():
    lst = CircularSinglyLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('a')
    assert lst.findFirst('a') == 0
    assert lst.findLast('a') == 2
    assert lst.findFirst('x') == -1
    assert lst.findLast('x') == -1
def test_clear():
    lst = CircularSinglyLinkedList()
    lst.append('a')
    lst.clear()
    assert lst.length() == 0

def test_extend():
    lst1 = CircularSinglyLinkedList()
    lst2 = CircularSinglyLinkedList()
    lst1.append('a')
    lst2.append('b')
    lst1.extend(lst2)
    assert lst1.length() == 2
    assert lst1.get(1) == 'b'
    lst2.append('c')
    assert lst1.length() == 2  # lst1 не змінюється при зміні lst2
