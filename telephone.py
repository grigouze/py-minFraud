#!/usr/bin/python

"""
Telephone verification of Maxmind
"""

from httpbase import HTTPBase

ALLOWED_FIELDS = ('l', 'phone', 'verify_code', 'language')

class Telephone(HTTPBase):
    """
    Class for telephone verification
    """

    def _init(self):
        """
        init of the main class
        """

        self.url = 'app/telephone_http'
        self.check_field = 'refid'
        self.timeout = 30
        # provide a default value of 10 seconds for timeout if not set by user

        for field in ALLOWED_FIELDS:
            self.allowed_fields[field] = 1
