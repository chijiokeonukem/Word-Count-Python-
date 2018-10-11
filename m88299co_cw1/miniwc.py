import sys

lineCount = 0
wordCount = 0
byteCount = 0

argCount = len(sys.argv)
if (argCount > 1):
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        for line in file:
            wordsList = line.split()
            lineCount +=1
            wordCount += len(wordsList)
            byteCount += len(line)

    print('\t' + lineCount , wordCount, "\t", byteCount, filename)

else:
    print("Please enter a file name")
