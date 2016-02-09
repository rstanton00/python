#Tuples

#like lists: values can be any type and indexed by integers
#are immutable (can't be changed) and also comparable and hashable
#so lists of them can be sorted and used as key values in dictionaries
#dictionary keys have to be tuples or strings (immutable types, basically)

#t = ('a', 'b', 'c')
#t = ('a',) for a single-element tuple you need the comma, otherwise python thinks this is a string
#t = tuple() as an alternative assignment, for which tuple('a') works
#t = tuple('word') yields ('w', 'o', 'r', 'd')
#t[0] would be 'w'
#t[1:3] would yield ('o', 'r')
#can't modify a tuple, but can replace one with another
#t = ('A',) + t[1:] yields ('A', 'o', 'r', 'd')

#To decorate in Python is to build a list of tuples with one or more sort keys preceding
#the elements from the sequence, like:
#t = list()
#for word in words:
#  t.append((len(word), word)) #build a list of tuples with sort keys preceding element

#can also do something like:
#addr = 'test@test.org'
#uname, domain = addr.split('@')

#Dictionaries have a method called items that returns a list of tuples, where each
#tuple is a key-value pair
#>>> d = {'a':10, 'b':1, 'c':22}
#>>> t = d.items()
#>>> print t
#[('a', 10), ('c', 22), ('b', 1)]
#Can sort a list of tuples, so converting from dictionary to tuple-list is useful
#A list of tuples is sorted by key value

#l=list()
#for key, val in dictionary.items():
  #l.append((val, key))
#l.sort(reverse=True)
#now l is a list sorted by the values that the keys hold

#Because tuples are hashable and lists are not, if we want to create a composite
#key to use in a dictionary we must use a tuple as the key:
#directory[last, first] = number (the expression in brackets is a tuple)
#traversal:
#for last, first in directory:
#  print first, last, directory[last, first]

#sorted and reversed work on all data structures (even immutable ones) and return a new copy

import string

def countNumOfCommits(myFile):
  try:
    fIn = open(myFile)
  except:
    print('File cant be opened: ', myFile)
    exit()
  dictIds = dict()
  resultList = list()
  for myLine in fIn:
    if myLine.startswith('From'):
      arrWords = myLine.split()
      if len(arrWords) > 3:
        dictIds[arrWords[1]] = dictIds.get(arrWords[1], 0) + 1
  for email, count in dictIds.items():
    resultList.append((count, email))
  resultList.sort(reverse=True)
  print(resultList[0])

if __name__ == "__main__":
  countNumOfCommits('mbox-short.txt')
