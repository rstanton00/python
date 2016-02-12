import re #for regular expressions

#if re.search('^From:', line) :
#  do stuff
#if re.search('F..m', line):
#  do stuff
#  matches F!@m, From, F12m, etc

#findall() is a function that will return all matches of the regex in the string
#line = line.rstrip()
#myResultList = re.findall('\S+@\S+', line)

#there is also re.search
#if re.search('^X\S*: [0-9]+', line)

#parens
#line = re.findall('^X\S*: ([0-9.]+)', line)
#this will return only the floating point portion of the matching string

#result = re.findall('ˆFrom .* ([0-9][0-9]):', line)

def grepPy(myFile, regEx):
  try:
    fIn = open(myFile)
  except:
    print('Could not open file', myFile)
    exit()
  count = 0
  for myLine in fIn:
    if re.search(regEx, myLine):
      count += 1
  print(myFile, 'had', count, 'lines that matched', regEx)


def revisionCount(myFile):
  try:
    fIn = open(myFile)
  except:
    print('Could not open file', myFile)
    exit()
  revCount = 0.0
  numRevs = 0
  for myLine in fIn:
    rev = re.findall('^New Revision:\s*(\d+)', myLine)
    if len(rev) > 0:
      revCount += float(rev[0])
      numRevs += 1
  print(revCount/numRevs)


if __name__ == "__main__":
  grepPy('mbox.txt', '^Author')
  revisionCount('mbox.txt')
