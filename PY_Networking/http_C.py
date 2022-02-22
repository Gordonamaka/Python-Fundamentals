# Creating a simple Web Browser in Python

# An example of an http request in Python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) ) # HOST, PORT - This will blowup if the software is not running (traceback error)


# We're the web browser in this case.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.1\n\n'.encode() # This sends the string across the network as we encode it into UTF-8
mysock.send(cmd) # And this receives it back

while True:
  data = mysock.recv(256) # Simple loop to receive 512 characters at a time.
  if ( len(data) < 1 ): # If we get 0 characters, the string is closed, and therefore we should end the line of communication (Socket). If the network is slow, the process will take awhile until the entire socket is closed.
    break
  print(data.decode()) # Have to decode it before we print it.
mysock.close() # Then we end the socket.