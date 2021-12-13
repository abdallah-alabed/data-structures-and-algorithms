from hashtables import __version__
import hashtables
from hashtables.hash import Hashtable
from hashtables.hash_repeted import repeatedWord

def test_version():
    assert __version__ == '0.1.0'

# Code Challenge 30

# Adding a key/value to your hashtable results in the value being in the data structure


def test_1():
    h = Hashtable()
    h.add('Abdallah', 100)
    assert h.contain('Abdallah') == True

# Retrieving based on a key returns the value stored


def test_2():
    h = Hashtable()
    h.add('Abdallah', 100)
    assert h.get('Abdallah') == 100

# Successfully returns null for a key that does not exist in the hashtable


def test_3():
    h = Hashtable()
    h.add('Abdallah', 100)
    assert h.get('Issa') == 'NULL'

# Successfully handle a collision within the hashtable


def test_4():
    h = Hashtable()
    h.add('ABD', 100)
    h.add('BAD', 50)
    assert h.contain('BAD') == True
    assert h.contain('ABD') == True

# Successfully retrieve a value from a bucket within the hashtable that has a collision


def test_5():
    h = Hashtable()
    h.add('ABD', 100)
    h.add('BAD', 50)
    assert h.get('BAD') == 50
    assert h.get('ABD') == 100

# Successfully hash a key to an in-range value


def test_6():
    h = Hashtable()
    assert h.hash('Abd') == 901

    # A = 65 , b=98 , d=100
    # 263*19=4997
    # 4997 % 1024= 901


# Code Challenge 31

def test_repeat_1():

    assert repeatedWord('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...') == 'summer'


def test_repeat_2():

    assert repeatedWord('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...') == 'it'


def test_repeat_3():
    
    assert repeatedWord(
        'Once upon a time, there was a brave princess who') == 'a'
