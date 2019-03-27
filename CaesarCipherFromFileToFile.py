# Getting Input from a file and running it through a caesar cipher and printing the output into a file.

import sys
import os


MAX_KEY_SIZE = 26


def getMode():
    while True:
	    print('Do you wish to encipher or decipher a message?')
        print('Enter either "encipher" or "e" or "decipher" or "d".')
        mode = raw_input().lower()
        return mode


def getMessage():
    user_file = raw_input("Enter the path of file.\n")

    assert os.path.exists(user_file), "File not found out at " +str(user_file)
    f = open(user_file,'r')
    txt = f.readline()
    return txt


def getKey():
    key = 0
    while True:
        print("Enter key value between (1-%s)" %(MAX_KEY_SIZE))
        key = int(raw_input())
        if(key >= 1 and key <= MAX_KEY_SIZE):
            return key


def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


mode = getMode()
message = getMessage()
key = getKey()


fh = open('CipheredText.txt','w')
fh.write(getTranslatedMessage(mode, message, key))
fh.close()
