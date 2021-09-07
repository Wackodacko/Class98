def countWordsFromFile():
    fileName=input("Enter The file name: ")

    numberOfwords=0

    file=open(fileName,'r')
    for line in file:
        words=line.split() 
        numberOfwords=numberOfwords+len(words)
    print("Number Of Words: ")
    print(numberOfwords)

countWordsFromFile()
