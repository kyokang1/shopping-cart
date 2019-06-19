#Shopping-cart-test.py

import os

from shopping_cart import to_usd

#import sys
#sys.path.append('../')
#from shopping_cart import to_usd

def test_to_usd():
    price = 4050.13
    assert to_usd(price) == "$4,050.13"


