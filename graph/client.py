#!/usr/bin/env python3

import socket, sys, re, os
from node import *
from bsonrpc import JSONRpc
sys.path.append("../lib")       # for params
import params

switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )


def get_socket(server):
    ''' Try establishing a socket connection to the sever. '''
    try:
        serverHost, serverPort = re.split(":", server)
        serverPort = int(serverPort)
    except:
        print("Can't parse server:port from '%s'" % server)
        sys.exit(1)

    s = None
    for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            print(" error: %s" % msg)
            s = None
            continue
        try:
            print(" attempting to connect to %s" % repr(sa))
            s.connect(sa)
        except socket.error as msg:
            print(" error: %s" % msg)
            s.close()
            s = None
            continue
        break
    return s

progname = "fileClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug  = paramMap["server"], paramMap["usage"], paramMap["debug"]

s = get_socket(server)

rpc = JSONRpc(s)
rpc_server = rpc.get_peer_proxy()

# create a tree
leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf1, leaf2])

root.show()

# Execute in rpc_server:
g, n = encodeGraph(root)
res_g, res_n = rpc_server.increment_graph(g, n)
result = decodeGraph(res_g, res_n)
result.show()

rpc.close() # Closes the socket 's' also


