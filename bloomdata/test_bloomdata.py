'''
This module is a pytest module for bloomdata.py
'''
from bloomdata.bloomdata import increment


def test_increment_int():
    '''
    This is a test function for integers and the increment function from bloomdata.py
    '''
    assert increment(3) == 4
    assert increment(-2) == -1

def test_increment_float():
    '''
    This is a test function for floats and the increment function from bloomdata.py
    '''
    assert increment(1.5) == 2.5
    assert increment(-0.5) == 0.5

def test_increment_int_return_type():
    assert isinstance(increment(3), int)