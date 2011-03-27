#!/usr/bin/python

"""
Location verification of Maxmind
"""

from minfraud.httpbase import HTTPBase

ALLOWED_FIELDS = ('i', 'city', 'region', 'postal', 'country')

class Location(HTTPBase):
    """
    Class for location verification
    """

    def _init(self):
        """
        init of the main class
        """

        self.url = 'app/locvr'
        self.check_field = 'distance'
        self.timeout = 30
        # provide a default value of 10 seconds for timeout if not set by user

        for field in ALLOWED_FIELDS:
            self.allowed_fields[field] = 1
