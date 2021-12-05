from insertion_sort import __version__
from insertion_sort.insertion_sort import sorted

def test_version():
    assert __version__ == '0.1.0'

def test_1():
    arr=[8,4,23,42,16,15]
    assert sorted(arr) == [4,8,15,16,23,42]

def test_2():
    arr=[20,18,12,8,5,-2]
    assert sorted(arr) == [-2,5,8,12,18,20]

def test_3():
    arr=[5,12,7,5,5,7]
    assert sorted(arr) == [5,5,5,7,7,12]

def test_4():
    arr=[2,3,5,7,13,11]
    assert sorted(arr) == [2,3,5,7,11,13]