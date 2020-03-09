


def getGeneratedKeyVig(word):
    vigGlobalKey = "CRYKEYUNIQUE"
    generatedKey, currIndex = "", 0
    for i in range(len(word)):
        if (currIndex >= len(vigGlobalKey)):
            currIndex = 0
        generatedKey += vigGlobalKey[currIndex]
        currIndex += 1
    return generatedKey


def encVig(word):
    encWord = ""
    genKey = getGeneratedKeyVig(word)
    word.upper()
    for i in range(len(word)):
        if (word[i].islower()):
            encWord += chr(((ord(word[i].upper()) - 65) + (ord(genKey[i]) - 65)) % 26 + 65)
        else:
            encWord += chr(((ord(word[i]) - 65) + (ord(genKey[i]) - 65)) % 26 + 65)
    return encWord

def decVig(word):
    decWord = ""
    genKey = getGeneratedKeyVig(word)
    for i in range(len(word)):
        decWord += chr(((ord(word[i]) - 65) - (ord(genKey[i]) - 65) + 26) % 26 + 65)
    return decWord


def encAffine(word):
    encWord, a, b = "", 17, 20
    ''' 
        C = (a*x + b) % 26 
    '''
    for i in range(len(word)):
        if (word[i].islower()):
            encWord += chr(((a * ord(word[i].upper()) - 65) + b) % 26 + 65)
        else:
            encWord += chr(((a * ord(word[i]) - 65) + b) % 26 + 65)

    return encWord

def decAffine(word):
    decWord, a, b ,aInverse= "", 17, 20, 0

    for i in range(26):
        if ((a * i) % 26) == 1:
            aInverse = i
    ''' 
       x = (a^-1 * (C - b)) % 26 
    '''
    for i in range(len(word)):
        decWord += chr(((aInverse * (ord(word[i]) - b - 65)) % 26) + 65)
    return decWord


def encShift(input):
    output, s = "", 4

    for i in range(len(input)):

        if (input[i].isupper()):
            output += chr((ord(input[i]) + s - 65) % 26 + 65)
        else:
            output += chr((ord(input[i]) + s - 97) % 26 + 97)
    return output


def decShift(input):
    output, s = "", 4
    for i in range(len(input)):

        if (input[i].isupper()):
            output += chr((ord(input[i]) - s - 65) % 26 + 65)
        else:
            output += chr((ord(input[i]) - s - 97) % 26 + 97)
    return output




affineWord =encAffine("MOSTAFA")
print (affineWord)
print(decAffine(affineWord))
print ("------------------------------\n")

Word =encShift("MOSTAFA")
print (Word)
print(decShift(Word))
print ("------------------------------\n")


Word =encVig("MOSTAFA")
print (Word)
print(decVig(Word))
print ("------------------------------\n")
