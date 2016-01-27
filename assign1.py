total = 0
myList = []
while True:
  myIn = input("Input a digit:  ")
  if myIn == "done":
    print("# of elements in list: ", len(myList), "\n")
    print("average of list elements: ", float(total)/len(myList), "\n")
    print("total of list elements: ", total, '\n')
    break
  else:
    myList.append(int(myIn))
    total += int(myIn) 
