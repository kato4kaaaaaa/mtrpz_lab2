import pytest
from array_based_list import ArrayBasedList

def test_append_and_length():
    lst = ArrayBasedList()
    assert lst.length() == 0
    lst.append('a')
    lst.append('b')
    assert lst.length() == 2
    assert lst.get(0) == 'a'
    assert lst.get(1) == 'b'

def test_insert_and_get():
    lst = ArrayBasedList()
    lst.append('a')
    lst.append('c')
    lst.insert('b', 1)
    assert lst.get(1) == 'b'
    assert lst.length() == 3
def test_insert_invalid_index():
    lst = ArrayBasedList()
    with pytest.raises(IndexError):
        lst.insert('x', -1)
    with pytest.raises(IndexError):
        lst.insert('x', 1)

def test_get_invalid_index():
    lst = ArrayBasedList()
    with pytest.raises(IndexError):
        lst.get(0)
    lst.append('a')
    with pytest.raises(IndexError):
        lst.get(1)

def test_delete_invalid_index():
    lst = ArrayBasedList()
    with pytest.raises(IndexError):
        lst.delete(0)
    lst.append('a')
    with pytest.raises(IndexError):
        lst.delete(1)
