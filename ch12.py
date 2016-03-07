import socket

#create an INET, streaming socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the web server on port 80, the normal http port
mysock.connect(('www.py4inf.com', 80))
msg='GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'
totalsent=0
#mysock.send(b"msg")
mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

#works on linux, but apparently not mac?
while True:
  print("in while loop")
  data = mysock.recv(512)
  if ( len(data) < 1 ) :
    break
  print("data is ", data)

#close socket to the webserver
mysock.close()

#1
