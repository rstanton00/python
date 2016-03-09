import socket
import time

#create an INET, streaming socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the web server on port 80, the normal http port
mysock.connect(('www.py4inf.com', 80))
totalsent=0

#would be interested in knowing how to put the GET part into a variable
mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
  #receive data in 512 byte chunks from the socket
  #recv returns an empty string when there is no more data to read
  data = mysock.recv(512)
  if ( len(data) < 1 ) :
    break
  print("data is\n", data.decode())

#close socket to the webserver
mysock.close()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send(b'GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')
count = 0
picture = "";
while True:
  data = mysock.recv(5120)
  if ( len(data) < 1 ) : break
  # time.sleep(0.25)
  count = count + len(data)
  print(len(data), count)
  picture = picture + data.decode()
mysock.close()

#1
