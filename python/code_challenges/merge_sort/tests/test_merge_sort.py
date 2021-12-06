from merge_sort import __version__
from merge_sort.mergesort import mergeSort

def test_version():
    assert __version__ == '0.1.0'

def test_1():
    assert mergeSort([8,4,23,42,16,15]) == [4,8,15,16,23,42]

def test_2():
    assert mergeSort([20,18,12,8,5,-2]) == [-2,5,8,12,18,20]

def test_3():
    assert mergeSort([5,12,7,5,5,7]) == [5,5,5,7,7,12]

def test_4():
    assert mergeSort([2,3,5,7,13,11]) == [2,3,5,7,11,13]