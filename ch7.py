try:
  inFile = input('Enter the file name: ')
  type = input('Enter <upper> or <search> for type of program to run: ')
except:
  print('Inappropriate number of arguments supplied')
  exit()

try:
  fIn = open(inFile)
except:
  print('File cannot be opened: ', inFile)
  exit()

confTotal = 0.0
countConf = 0
for line in fIn:
  if (type == 'upper'):
    print(line.strip().upper())
  if (type == 'search'):
    if 'X-DSPAM-Confidence: ' in line:
      confTotal += float(line[line.strip().find(':')+1:])
      countConf += 1

if (type == 'search'):
  print(confTotal/float(countConf))

#text examples, commented out
  
#try:
#  fin = open(input('Enter the file name: '))
#except:
#  print('File cannot be opened') 
#  exit()

#try:
#  count = 0
#  for line in fin:
#    count = count+1
#    #skip lines we aren't interested in
#    if not line.startswith('From:'):
#      continue
#    #process interesting line
#    if line.find('@uct.ac.za') == -1:
#      continue
#    print(line.strip())
#  print('line count: ', count)
#except:
#  print('An exception occurred')

#to bring the entire file into memory, do:
#fin = open('mbox.txt')
#input = fin.read()

#When the file is read in this manner, all the characters including all of the lines
#and newline characters are one big string in the variable

#print len(inp) prints the number of characters
#print input[:20] yields the first 20 characters 

#to open a file for writing, do
#fout = open('out.txt', 'w')
#fout.write("test text\n")
#fout.close()  --must close the file to officially write it to disk
