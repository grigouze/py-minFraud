#!/usr/bin/python

import hashlib
from creditcard import CreditCard

if __name__ == '__main__':
    aa = CreditCard()
    aa.input( { 'city': 'New York' } )
    aa.query()
    print aa.output()
