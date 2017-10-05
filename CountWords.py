
FILEPATH = 'myFile.txt'

File = open(FILEPATH, 'r')
Sum = 0
line = File.readline()
while line:
    words = line.split(' ')
    print words
    Sum += len(words)
    line = File.readline()
File.close()
print Sum
