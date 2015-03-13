#!/usr/bin/env python
import socket
import sys


port = 8000
host = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print " Server start scucessful "

while 1:
    clientsocket, clientaddr  = s.accept()
    clientfile = clientsocket.makefile('rw', 0)
    clientfile.write("HI  got u " + str(clientaddr) + '\n')
    clientfile.write("guess sth ")
    line = clientfile.readline()
    clientfile.write("y think %s" % line)
    clientfile.close()
    clientsocket.close()
