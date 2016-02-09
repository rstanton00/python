def chop (myList):
  myList.pop(0) #remove first element
  myList.pop() #remove last element

def middle(myList):
  return myList[1:-1] #return a new list with all but the first and last elements

def romeo(myFile):
  fIn = open(myFile)
  words = []
  for myLine in fIn:
    print(myLine)
    lineWords = myLine.split(' ')
    for word in lineWords:
      print(word)
      if word in words:
        continue
      else:
        print("Appending: ", word)
        words.append(word)
  words.sort()
  return words

def fromcount(myFile):
  fIn = open(myFile)
  fromL = []
  for myLine in fIn:
    lineWords = myLine.split(' ')
    if lineWords[0] == 'From':
      fromL.append(lineWords[1])
      print(lineWords[1])
  print(len(fromL))

if __name__ == "__main__":
  aList = [1, 2, 3, 4, 5]
  #chop(aList)
  #print(aList)
  #print(middle(aList))
  #print(aList)
  #print(romeo('romeo.txt'))
  fromcount('mbox-short.txt')

#python has nested lists
#myList = ['spam', 2.0, 5, [10, 20]]

#change lists via indexing
#myList[0] = 3.3

#if you try to access something that doesn't exist, you get
#an IndexError

#if 5 in myList:
#  print('Found 5!')

#if you want to only read the elements of a list, do:
#for i in myList:
#  print(i)

#if you want to write or update the elements, need the indices
#so use range and len to get them
#for i in range(len(myList)):
#  myList[i] = myList[i] * 2

#the + operator concatenates lists
#the slice operator works on lists, ie myList[1:3]

#lists have .append(element) and .extend(lists)

#myList.pop(1) modifies the list and returns the element that was removed
#if you don't provide an index, it deletes and returns the last element

#myList.remove('b') removes the element you want, assuming you don't know the index

#can also use del to remove a number of elements, ie del myList[1:2]

#also myList.sort()

#sum(myList), max(myList), and len(myList) also work

#strings have a split method (string.split('/t') to split on tab delimited
#strings also have join using a string delimiter and a list of strings to merge together

#Python is pass by reference, so functions always get references to objects/variables/etc
