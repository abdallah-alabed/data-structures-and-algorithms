from quick_sort import __version__
from quick_sort.quick_sort import QuickSort

def test_version():
    assert __version__ == '0.1.0'

def test_1():
    assert QuickSort([8,4,23,42,16,15],0,5) == [4,8,15,16,23,42]

def test_2():
    assert QuickSort([20,18,12,8,5,-2],0,5) == [-2,5,8,12,18,20]

def test_3():
    assert QuickSort([5,12,7,5,5,7],0,5) == [5,5,5,7,7,12]

def test_4():
    assert QuickSort([2,3,5,7,13,11],0,5) == [2,3,5,7,11,13]
