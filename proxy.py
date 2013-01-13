import os
import argparse
import select
import Queue
from socket import *

DELAY = 0.0001
BUFFER_SIZE = 4096

class Proxy:

    input = []

    def __init__(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.setblocking(0)
        self.server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        arg = self.getargs()
        self.server.bind((arg[1], arg[0]))
        self.server_sock.listen(300)
        self.message_queues = {}

    def getargs(self):
        parser = argparse.ArgumentParser(description='Caching Web Proxy. Default host is localhost, default port is 1234')
        parser.add_argument('-p', '--port', help = 'port', type=int)
        parser.add_argument('-s', '--host', help = 'host')
        args = parser.parse_args()
        port = 1234
        host = 'localhost'
        if args.port: port = args.port
        if args.host: host = args.host
        return port, host
    
    def main(self):




    def handler(self, client_sock):
        request = client_sock.recv(1049000)
        url = request.split(' ')[1]
        pos = url.find("://")
        clihost = url[(pos+3):]
        opos = clihost.find("/")
        trueurl = clihost[:opos]

        try:
            s = socket(AF_INET, SOCK_STREAM)  
            s.connect((trueurl, 80))
            s.send(request)

            while True:
                serverdata = s.recv(1049000)
                if not serverdata: break
                else:
                    client_sock.send(serverdata)
                    s.close()
                    client_sock.close()
            
        except error, (value, message):
            if s:
                s.close()
            if client_sock:
                client_sock.close()
            print "Runtime Error:", message
            sys.exit(1)


if __name__ == '__main__':
    p = Proxy()
    sys.exit(p.main())
