total = 0
myList = []
while True:
  myIn = input("Input a digit:  ")
  try:
    if myIn == "done":
      print("# of elements in list: ", len(myList), "\n")
      print("average of list elements: ", float(total)/len(myList), "\n")
      print("total of list elements: ", total, '\n')
      break
    else:
      myList.append(int(myIn))
      total += int(myIn)
  except:
    print("Bad data")


total=0
myList = []
while True:
  myIn = input("Input a digit: ")
  try:
    if myIn == "done":
      myList.sort()
      print('Min value in list is: ', myList[0])
      print('Max value in list is: ', myList[len(myList)-1])
      break
    else:
      myList.append(int(myIn))
  except:
    print('Invalid entry')
