# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from node import *
from bsonrpc import JSONRpc
from bsonrpc import request, service_class

# Class providing functions for the client to use:
@service_class
class ServerServices(object):

    @request
    def nop(self, txt):
        print(txt)
        return txt

    @request
    def increment_graph(self, graph, nodes):
        root = decodeGraph(graph, nodes) # rebuild graph
        increment(root)
        newGraph, newNodes = encodeGraph(root)
        return newGraph, newNodes

# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
    s, _ = ss.accept()
    # JSONRpc object spawns internal thread to serve the connection.
    JSONRpc(s, ServerServices())
Client

