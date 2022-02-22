# Networked Programs

"""
Transport Control Protocol (TCP)
- Built on top of IP (Internet Protocol)
- Assumes IP might lose some data. Stores and retransmits data if it seems to be lost
- Hanldes "Flow control" using a transmit window
- Provides a nice reliable pipe

TCP Connections / Sockets
In computer newtowrking, an internet socket or network socket is an endpoint of a bidrectional inter-process communication flow across an internet Protocol-based computer network, such as the internet.

Socket connection simplified
Process - Internet - Process

TCP Port Numbers
- A port is an application-specific or process specific software communications endpoint
- It allows multiple networked applications to coexist on the same server.
- There is a list of well-known TCP port numbers

"""

# Python has built-in support for TCP sockets - Relatively simple compared to Javascript
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) ) # HOST, PORT