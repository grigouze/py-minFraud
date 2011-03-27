#!/usr/bin/python

"""
Tests for Location
"""

from minfraud.location import Location

if __name__ == '__main__':
    aa = Location()
    aa.input( { 'phone': 'New York' } )
    aa.query()
    print aa.output()
