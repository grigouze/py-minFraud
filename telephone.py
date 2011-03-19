#!/usr/bin/python

"""
"""

from httpbase import HTTPBase

ALLOWED_FIELDS = ('l', 'phone', 'verify_code', 'language')

class Telephone(HTTPBase):
    """
    """
    def _init(self):
        """
        """
        self.url = 'app/telephone_http'
        self.check_field = 'refid'
        self.timeout = 30
        # provide a default value of 10 seconds for timeout if not set by user

        for field in ALLOWED_FIELDS:
            self.allowed_fields[field] = 1

if __name__ == '__main__':
    aa = Telephone()
    aa.input( { 'phone': 'New York' } )
    aa.query()
    print aa.output()
