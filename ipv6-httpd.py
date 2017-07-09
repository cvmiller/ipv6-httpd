#!/usr/bin/env python3

"""
    Python 3 webserver which supports IPv6
    original from:
        https://gist.github.com/akorobov/7903307
    
    Pseudo path of /ip will report client IP address back to client, 
        otherwise, shows directory index

    Modified to work under python3 by Craig Miller 23 June 2017
    Version 0.92
"""

#
# Issue for python 3.4 when ^C is pressed to quit server 
#   http://bugs.python.org/issue14574
#


# port webserver listens to
listen_port = 8080

import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

import signal
import sys

# setup global for server request loop
shutdown_requested = False

# signal handlder for SIGINT
def sigint_handler(signal, frame):
    global shutdown_requested
    shutdown_requested = True
    print("Caught SIGINT, dying")
    sys.exit(0)

# register SIGINT signal handler
signal.signal(signal.SIGINT, sigint_handler)


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # if path is /ip then print client IP address (v4 or v6)
        if self.path == '/ip':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            answer = 'Your IP address is ' + self.client_address[0]
            # convert string 'answer' to binary for buffer output
            self.wfile.write(str.encode(answer))
            return
        else:
            return SimpleHTTPRequestHandler.do_GET(self)

class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6

def main():
    server = HTTPServerV6(('::', listen_port), MyHandler)
    print('Press ^C to quit')
    while not shutdown_requested:
        try:
            server.handle_request()
        except:
            # get out of loop
            pass
    sys.exit(0)


if __name__ == '__main__':
    main()
