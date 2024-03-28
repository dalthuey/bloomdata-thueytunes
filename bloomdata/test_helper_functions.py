'''
This module is a pytest module for helper_functions.py
Note single '_' in test... .py filename
'''
import pytest
from bloomdata import helper__functions as hf

adjectives = ['blue', 'large', 'grainy', 
              'substantial', 'potent', 'thermonuclear']

nouns = ['food', 'house', 'tree', 
         'bicycle', 'toupee', 'phone']

list1 = [1, 2, 3]

list2 = [4, 5, 6]

def test_random_phrase():
    '''
    This is a test function for strings and the random_phrase function from helper__functions.py
    '''
    assert isinstance(hf.random_phrase(adjectives, nouns), str)
    assert isinstance(hf.random_phrase(list1, list2), str)