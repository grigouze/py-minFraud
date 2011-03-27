#!/usr/bin/python

"""
Tests for Location
"""

from minfraud.location import Location

if __name__ == '__main__':
    aa = Location()
    input = {
        'i': '24.24.24.24',
        'city': 'NewYork',
        'region': 'NY',
        'postal': '10011',
        'country': 'US',
    }
    aa.input( input )
    aa.query()
    print aa.output()
