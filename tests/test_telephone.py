#!/usr/bin/python

"""
"""

from telephone import Telephone

if __name__ == '__main__':
    aa = Telephone()
    aa.input( { 'phone': 'New York' } )
    aa.query()
    print aa.output()
