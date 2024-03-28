'''
This module is a pytest module for wallet.py
'''
import pytest
from bloomdata.wallet import Wallet as wlt

@pytest.fixture
def empty_wlt():
    '''
    This fixture returns an empty wallet
    '''
    return wlt()

@pytest.fixture
def wlt_20():
    '''
    This fixture returns a wallet with a balance of $20
    '''
    return wlt(20)

def test_empty_wlt(empty_wlt):
    '''
    This function tests if an empty wallet's balance matches an amount of 0
    '''
    assert empty_wlt.balance == 0

def test_wlt_20(wlt_20):
    '''
    This function tests if a wsallet's balance matches an amount of 20
    '''
    assert wlt_20.balance == 20

def test_wlt_20_spend_10(wlt_20):
    '''
    This function tests if a wallet with a balance of $20 matches the amount of 10
    After spending $10
    '''
    assert wlt_20.withdraw(10) == "Remaining balance after withdrawal: $10"
    assert wlt_20.balance == 10

def test_wlt_spend_all(wlt_20):
    '''
    This function tests if a wallet with a balance of $20 matches an amount of 0
    After spending $20
    '''
    assert wlt_20.withdraw(20) == "Remaining balance after withdrawal: $0"
