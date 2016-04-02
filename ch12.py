import socket
import time
import re
from urllib.request import urlopen

#for Beautiful Soup
from bs4 import *

#create an INET, streaming socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the web server on port 80, the normal http port
#mysock.connect(('www.py4inf.com', 80))
#totalsent=0

#would be interested in knowing how to put the GET part into a variable
#mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

#while True:
  #receive data in 512 byte chunks from the socket
  #recv returns an empty string when there is no more data to read
#  data = mysock.recv(512)
#  if ( len(data) < 1 ) :
#    break
#  print("data is\n", data.decode())

#close socket to the webserver
#mysock.close()


#this is not working
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('www.py4inf.com', 80))
#mysock.send(b'GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')
#count = 0
#initialize picture an empty byte string, because we are adding 
#data (in bytestring) to it with each iteration of the loop
#picture = b'';
#while True:
#  data = mysock.recv(5120)
#  if ( len(data) < 1 ) : break
  # time.sleep(0.25)
#  count = count + len(data)
#  print(len(data), count)
#  picture = picture + data
#mysock.close()

# Look for the end of the header (2 CRLF)
#pos = picture.find(b"\r\n\r\n");
#print('Header length', pos)
#print(picture[:pos])

# Skip past the header and save the picture data
#picture = picture[pos+4:]
#fhand = open("stuff.jpg","wb")
#fhand.write(picture);
#fhand.close()

counts = dict()
fhand = urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
  print(line.strip().decode())
  words = line.split()
  for word in words:
    counts[word.decode()] = counts.get(word.decode(), 0) + 1
print(counts)

#url = input('Enter - ')
#html = urlopen(url).read()
#links = re.findall('href="(http://.*?)"', html.decode())
#for link in links:
#  print(link)
#soup = BeautifulSoup(html, 'html.parser')
#soup = BeautifulSoup(html, "html.parser")

#print('LINKS')
#retrieve all of the anchor tags
#for link in soup.find_all('a'):
#  print(link.get('href'))
#  print('Content: ', link.contents[0])
#  print('Attrs: ', link.attrs)

#print('TEXT')
#print(soup.get_text())

#download an image
#img = urlopen('http://www.py4inf.com/cover.jpg')
#fhand = open('cover.jpg', 'wb')
#size = 0
#while True:
#  info = img.read(100000)
#  if len(info) < 1 : break
#  size = size + len(info)
#  fhand.write(bytes(info))

#print(size, 'characters copied.')
#fhand.close()


def socketProg1():
  url = input('Enter a url - ')

  try:
    re.search('^http\:\/\/www\.\w+\.\w+$', url)
  except:
    print('URL entered was not valid: ', url)
    exit()

  urlPieces = url.split('/')
  #create an INET, streaming socket
  mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  #connect to the web server on port 80, the normal http port
  print('url piece 2: ', urlPieces[2])
  mysock.connect((urlPieces[2], 80))
  
  totalsent=0
  mysock.send(b'GET '.join([bytes(url, 'utf8'), b' HTTP/1.0\n\n']))

  while True:
    #receive data in 512 byte chunks from the socket
    #recv returns an empty string when there is no more data to read
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
      break
    print("data is\n", data.decode())

  #close socket to the webserver
  mysock.close()


def socketProg3():
  url = input('Enter a url - ')
  try:
    re.search('^http\:\/\/www\.\w+\.\w+$', url)
  except:
    print('URL entered was not valid: ', url)
    exit()

  charCount = 0
  fIn = urlopen(url)
  for line in fIn:
    line = line.strip().decode()
    print('line: ', line)
    words = line.split()
    for word in words:
      for char in word:
        charCount += 1
        if charCount <= 3000:
          print(char)
  print(charCount)


if __name__ == "__main__":
  #socketProg1()
  socketProg3()
