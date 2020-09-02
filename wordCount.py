import sys
import re
import string
if len(sys.argv) is not 3:
    print("Please enter: wordCountTest.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]

wordList = {}
outputList = []
textFile = open(textFname, "r")
wordsInFile = {}
temp = 0
for line in textFile:
    line = line.lower().strip()
    line = line.replace('-', " ")
    line = line.replace("'", " ")
    word = re.split('[ \t]', line)
    for i in range(len(word)):
        word[i] = word[i].translate(None, string.punctuation) #used to strip punuations
        if word[i] in wordsInFile:
            temp = wordsInFile.get(word[i]) + 1
            wordsInFile[word[i]] = temp
        else:
            wordsInFile[word[i]] = 1
del wordsInFile[''] #deletes all new lines from dict
sorted_dict = sorted(wordsInFile.items())
outputFile = open(outputFname, "w")
for x, y in sorted_dict:
    outputFile.write(str(x) + ' ' + str(y) + '\n')
outputFile.close()
