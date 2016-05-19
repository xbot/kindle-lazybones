#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
     .-.     _
    (   `. .' )
     `\  `  .'
       |   |
       |   |
       | 66|_
       |  ,__)
       |(,_|
       | | 
       | \_,
       |   |
       |   |
     .'     \
    (    ,   )
     '--' '-'

Kindle Lazybones

Remote controlling utilities for kindle.

Author:  "Donie Leigh" <donie.leigh@gmail.com>
URL:     https://github.com/xbot/kindle-lazybones
License: Free Ware
"""

import time, os, re
import urlparse
import mimetypes
import BaseHTTPServer


HOST_NAME = ''
PORT_NUMBER = 8080
LAZYBONES_HOME = os.path.split(os.path.realpath(__file__))[0]


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(s):
        """Respond to a GET request."""
        pathInfo = urlparse.urlparse(s.path)
        if cmp(pathInfo.path, '/') == 0:
            s.indexAction()
        elif cmp(pathInfo.path, '/nextPage') == 0:
            s.send_response(200)
            os.system('cat ' + LAZYBONES_HOME + '/data/nextpage.dat > /dev/input/event0')
        elif cmp(pathInfo.path, '/prevPage') == 0:
            s.send_response(200)
            os.system('cat ' + LAZYBONES_HOME + '/data/prevpage.dat > /dev/input/event0')
        elif re.match(r'^/static/.*\.[a-zA-Z]+$', pathInfo.path):
            s.fetchResource(pathInfo.path)
        else:
            s.send_response(404)

    def indexAction(s):
        """The index page."""
        try:
            fp = open(LAZYBONES_HOME + '/view/index.html')
        except IOError:
            s.send_response(404)
        else:
            content = fp.read()
            fp.close()
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(content)

    def fetchResource(s, relPath):
        """Fetch a file."""
        fullPath = LAZYBONES_HOME + relPath
        try:
            fp = open(fullPath)
        except IOError:
            s.send_response(404)
        else:
            content = fp.read()
            fp.close()
            s.send_response(200)
            s.send_header("Content-type", mimetypes.guess_type(fullPath)[0])
            s.end_headers()
            s.wfile.write(content)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), RequestHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
