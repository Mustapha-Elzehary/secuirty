import sys
from os import open




def encShift(inFilePath, outFilePath, shift):
    fileIn = open(inFilePath, "r")
    fileOut = open(outFilePath, "a")
    shift %= 26
    outString = ""

    for eachLine in fileIn:
        for eachChar in eachLine:
            if eachChar == "\n" or eachChar == " " or eachChar.isdigit():
                outString += eachChar

            if (eachChar.isupper()):
                outString += chr((ord(eachChar) + shift - 65) % 26 + 65)
            else:
                outString += chr((ord(eachChar) + shift - 97) % 26 + 97)


    fileOut.write(outString);


def decShift(inFilePath, outFilePath, shift):

    fileIn = open(inFilePath, "r")
    fileOut = open(outFilePath, "a")
    shift %= 26
    outString = ""

    for eachLine in fileIn:
        for eachChar in eachLine:
            if eachChar == "\n" or eachChar == " " or eachChar.isdigit():
                outString += eachChar

            if (eachChar.isupper()):
                outString += chr((ord(eachChar) + shift - 65) % 26 + 65)
            else:
                outString += chr((ord(eachChar) + shift - 97) % 26 + 97)

    fileOut.write(outString);



def encAffine(inFilePath, outFilePath, a, b):
    # Greatest common devisor
    for i in range(2, 27):
        if a % i == 0 and 26 % i == 0:
            return

    if gcd(a, 26) != 1:
        print ("The two numbers must have no common divisor")
        return

    fileIn = open(inFilePath, "r")
    fileOut = open(outFilePath, "a")
    outString = ""

    for eachLine in fileIn:
        for eachChar in eachLine:
            if eachChar.isalpha():
                if (eachChar.isupper()):
                    outString +=  chr(((a * (ord(eachChar.lower()) - 65)) + b) % 26 + 65).upper()
                else:
                    outString +=  chr(((a * (ord(eachChar) - 65)) + b) % 26 + 65)
            else:
                outString += eachChar

    fileOut.write(outString);

def decAffine(inFilePath, outFilePath, a, b):
    aInv = -1
    for i in range(1, 26):
        result = (i * a) % 26
        if result == 1:
            aInv =  i


    if(aInv == -1):
        return

    fileIn = open(inFilePath, "r")
    fileOut = open(outFilePath, "a")
    outString = ""

    for eachLine in fileIn:
        for eachChar in eachLine:
            if eachChar.isalpha():
                if (eachChar.isupper()):
                    outString += chr(((aInv * (ord(eachChar.lower()) - 65 - b))) % 26 + 65).upper()
                else:
                    outString += chr(((aInv * (ord(eachChar.lower()) - 65 - b))) % 26 + 65)
            else:
                outString += eachChar

    fileOut.write(outString);


def encVig(inFilePath, outFilePath, token):
    token = token.lower()
    fileIn = open(inFilePath, "r")
    fileOut = open(outFilePath, "a")
    outString = ""
    j = 0
    tokLen= len(token)

    for eachLine in fileIn:
        for eachChar in eachLine:
            if eachChar.isalpha():
                if (eachChar.isupper()):
                    outString += chr(((ord(eachChar.lower()) - 65) + (ord(++j%tokLen) - 65)) % 26 + 65).upper()
                else:
                    outString += chr(((ord(eachChar.lower()) - 65) + (ord(++j%tokLen) - 65)) % 26 + 65)
            else:
                outString += eachChar
                ++j

    fileOut.write(outString);


def decVig(inFilePath, outFilePath, token):
    if token.isalpha() is False:
        return
    token = token.lower()
    fileIn = open(inFilePath, "r")
    fileOut = open(outFilePath, "a")
    outString = ""
    j = 0
    tokLen= len(token)

    for eachLine in fileIn:
        for eachChar in eachLine:
            if eachChar.isalpha():
                if (eachChar.isupper()):
                    outString += chr(((ord(eachChar.lower()) - 65) - ord(++j%tokLen) - 65 + 26) % 26 + 65).upper()
                else:
                    outString += chr(((ord(eachChar.lower()) - 65) - ord(++j%tokLen) - 65 + 26) % 26 + 65)
            else:
                outString += eachChar
                ++j

    fileOut.write(outString);


def start():
    options = list(sys.argv)

    if len(options) < 6 :
        return

    if options[1] == "shift":
        if(options[2] == "enc"):
            encShift(options[3], options[4], options[5])
        else:
            decShift(options[3], options[4], options[5])



    if options[1] == "affine":
        if(options[2] == "enc"):
            encAffine(options[3], options[4], options[5], options[6])
        else:
            decAffine(options[3], options[4], options[5], options[6])


    if options[1] == "vigenere":
        if (options[2] == "enc"):
            encVig(options[3], options[4], options[5])
        else:
            decVig(options[3], options[4], options[5])




if __name__ == '__main__':
    start()





