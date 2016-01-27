def count(myString, myLetter):
  count = 0
  for letter in myString:
    if letter == myLetter:
       count += 1
  print(count)

if __name__ == "__main__":
  count("Whatchamacallit", 'a')
