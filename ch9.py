import string

def inWords(myFile):
  try:
    fIn = open(myFile)
  except:
    print('File cant be opened: ', myFile)
    exit()

  words = dict()
  for myLine in fIn:
    myLIne = myLine.lower().translate(str.maketrans('', '', string.punctuation))
    wordsArr = myLine.split(' ')
    i=0
    for word in wordsArr:
       words[word] = i
       i += 1
  print('Found this many words: ', len(words))

def letterCount():
  word = 'brontosaurus'
  d = dict()
  for c in word:
    d[c] = d.get(c,0) + 1
  print(d)

def dayCount(myFile):
  try:
    fIn = open(myFile)
  except:
    print('Unable to open file')
    exit()

  days = dict()
  for myLine in fIn:
    if myLine.startswith('From'):
      fromArr = myLine.split();
      if len(fromArr) >= 3:
        days[fromArr[2]] = days.get(fromArr[2], 0) + 1
  print(days)

if __name__ == "__main__":
  #inWords('words.txt')
  dayCount('mbox-short.txt')
