#!/usr/bin/python

import hashlib
from httpbase import HTTPBase

ALLOWED_FIELDS = ( 'i', 'domain', 'city', 'region', 'postal', 'country', \
    'bin', 'binName', 'binPhone', 'custPhone', 'license_key', \
    'requested_type', 'forwardedIP', 'emailMD5', 'shipAddr', 'shipCity' \
    'shipRegion', 'shipPostal', 'shipCountry', 'txnID', 'sessionID', \
    'usernameMD5', 'passwordMD5', 'user_agent', 'accept_language' )

class CreditCard(HTTPBase):
    """
    """

    def _init(self):
        self.url = 'app/ccv2r'
        self.check_field = 'score'
        self.timeout = 10

        for field in ALLOWED_FIELDS:
            self.allowed_fields[field] = 1

    def filter_field(self, name, value):
        """
        """

        if name == 'emailMD5':
            if '@' in value:
                return self.md5(value)

        if name in ('usernameMD5', 'passwordMD5'):
            if len(value) != 32:
                return self.md5(value)

        return value

    def md5(self, value):
        """
        """

        return hashlib.md5(value.lower()).hexdigest()

if __name__ == '__main__':
    aa = CreditCard()
    aa.input( { 'city': 'New York' } )
    aa.query()
    print aa.output()
