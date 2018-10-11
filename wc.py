def nn():
    import sys
    lineCount = 0
    wordCount = 0
    byteCount = 0
    space = "        "
    argCount = len(sys.argv)
    if (argCount > 1):
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            for line in file:
                wordsList = line.split()
                lineCount +=1
                wordCount += len(wordsList)
                byteCount += len(line)
        filename = filename[11:]
        p= "Hello"
        return p
        #print('{0} {1} {0} {2} {0} {3} {0} {4}'.format(space, lineCount, wordCount, byteCount, filename))

    else:
        p = "Please enter a file name"
        return p

# We add the boilerplate to make this module both executable and importable.
if __name__ == "__main__":
    import doctest
    # The following command extracts all testable docstrings from the current module.
    doctest.testmod()
    nn()