def count(myString, myLetter):
  count = 0
  for letter in myString:
    if letter == myLetter:
       count += 1
  print("Found", myLetter, count, "times")

def parseString(myString):
  subString = myString[myString.find(':')+1:]
  print("The confidence score was: ", float(subString.strip()))

if __name__ == "__main__":
  count("Whatchamacallit", 'a')
  parseString('X-DSPAM-Confidence: 0.8475')
