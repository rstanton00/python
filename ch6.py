def count(myString, myLetter):
  count = 0
  for letter in myString:
    if letter == myLetter:
       count += 1
  print(count)

def parseString(myString):
  subString = myString[myString.find(':')+1:]
  print(float(subString.strip()))

if __name__ == "__main__":
  count("Whatchamacallit", 'a')
  parseString('X-DSPAM-Confidence: 0.8475')
