from hashtables import __version__
import hashtables
from hashtables.hash import Hashtable


def test_version():
    assert __version__ == '0.1.0'

### Code Challenge 30 

# Adding a key/value to your hashtable results in the value being in the data structure
def test_1():
    h=Hashtable()
    h.add('Abdallah',100)
    assert h.contain('Abdallah') == True

# Retrieving based on a key returns the value stored
def test_2():
    h=Hashtable()
    h.add('Abdallah',100)
    assert h.get('Abdallah') == 100

# Successfully returns null for a key that does not exist in the hashtable
def test_3():
    h=Hashtable()
    h.add('Abdallah',100)
    assert h.get('Issa') == 'NULL'

# Successfully handle a collision within the hashtable
def test_4():
    h=Hashtable()
    h.add('ABD',100)
    h.add('BAD',50)
    assert h.contain('BAD') == True
    assert h.contain('ABD') == True

# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_5():
    h=Hashtable()
    h.add('ABD',100)
    h.add('BAD',50)
    assert h.get('BAD') == 50
    assert h.get('ABD') == 100

# Successfully hash a key to an in-range value
def test_6():
    h=Hashtable()    
    assert h.hash('Abd') == 901

    # A = 65 , b=98 , d=100
    # 263*19=4997
    # 4997 % 1024= 901
