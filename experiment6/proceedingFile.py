import time
import calendar

FILEPATH = '../file.txt'
origin = open(FILEPATH, 'r')

for line in origin:
    print line
    line = line.split(' ')
    newFile = open(line[3]+'.txt', 'a')
    newTime = time.strptime(line[0]+line[1], '%Y-%m-%d%H:%M:%S')
    epochTime = calendar.timegm(newTime)
    userNum = line[5]
    newFile.write(str(epochTime)+':'+userNum+'\n')
    newFile.close()

origin.close()
