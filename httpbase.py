#!/usr/bin/python

"""
Base class for all Maxmind interaction
"""

DEFAULTSERVERS = ( 'minfraud3.maxmind.com', 'minfraud1.maxmind.com' \
    'minfraud2.maxmind.com' )

import urllib
import urllib2

class HTTPBase(object):
    """
    Base class
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

    def _init(self):
        """
        you have to subclass httpbase !
        """

        raise NotImplementedError

    def query(self):
        """
        send the query to maxmind server
        """

        if self.useDNS != 1:
            print "bla"

        for server in self.servers:
            result = self.querySingleServer(server)
            if result:
                return result
        return 0

    def input(self, inputs):
        """
        set the information to send for verification
        """

        if not inputs:
            inputs = {}

        for key, value in inputs.items():
            if not self.allowed_fields.get(key):
                raise 'truc'
            self.queries[key] = self.filter_field(key, value)

    def filter_field(self, name, value):
        """
        base function for filtering
        """

        return value

    def output(self):
        """
        Output of maxmind service
        """

        return self._output

    def querySingleServer(self, server):
        """
        Send the information to maxmind in http
        """

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

        f = urllib2.urlopen(url, qs, timeout)

        content = f.read()

        #print content

        kvpair = content.split(';')

        output = {}
        for kvp in kvpair:
            key, value = kvp.split('=', 2)
            output[key] = value

        self._output = output

        return 1
