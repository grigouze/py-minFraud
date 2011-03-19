#!/usr/bin/python

"""
"""

DEFAULTSERVERS = ( 'minfraud3.maxmind.com', 'minfraud1.maxmind.com' \
    'minfraud2.maxmind.com' )

from datetime import time

import urllib
import urllib2

class HTTPBase(object):
    """
    """

    url = ''
    check_field = ''
    timeout = ''
    allowed_fields = {}
    servers = []
    wsIpaddrRefreshTimeout = 0
    useDNS = 1
    isSecure = 1
    queries = {}
    _output = {}

    def __init__(self):
        for server in DEFAULTSERVERS:
            self.servers.append( server )

        if not self.wsIpaddrRefreshTimeout:
            self.wsIpaddrRefreshTimeout = 18000 # default of 5 hours timeout

        self.wsIpaddrCacheFile = '/tmp/maxmind.ws.cache'
        self._init()

    def query(self):
        if self.useDNS != 1:
            print "bla"

        for server in self.servers:
            result = self.querySingleServer(server)
            if result:
                return result
        return 0

    def input(self, vars={}):
        for k, v in vars.items():
            if not self.allowed_fields.get(k):
                raise 'truc'
            self.queries[k] = self.filter_field(k, v)

    def filter_field(self, name, value):
        return value

    def output(self):
        return self._output

    def querySingleServer(self, server):
        if self.isSecure == 1:
            proto = 'https'
        else:
            proto = 'http'

        url = '%s://%s/%s' % ( proto, server, self.url )
        check_field = self.check_field
        queries = self.queries
        queries.update({ 'clientAPI': 'Python/1.51' })

        if self.timeout > 0:
            timeout = self.timeout
        else:
            timeout = 0

        qs = urllib.urlencode(queries)
        #print "%s:%s" % ( url, qs )

        f = urllib2.urlopen(url, qs, self.timeout)

        content = f.read()

        #print content

        kvpair = content.split(';')

        output = {}
        for kvp in kvpair:
            key, value = kvp.split('=', 2)
            output[key] = value

        self._output = output

        return 1
