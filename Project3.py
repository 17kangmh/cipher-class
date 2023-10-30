# File: Project3.py
# Student: Minhyuk Kang 
# UT EID:mk44496
# Course Name: CS303E
# 
# Date:11/29
# Description of Program: This program implements a substitution cipher class.

import random
import os

# A global constant defining the alphabet. 
LETTERS = "abcdefghijklmnopqrstuvwxyz"

# You are welcome to use the following two auxiliary functions, or 
# define your own.   They use some constructs we haven't covered. 

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LETTERS.
    key = key.lower()
    return ( len(key) == 26 and all( [ ch in key for ch in LETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LETTERS.
    lst = list( LETTERS )    # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey() ):
        self.__key = key
        """Create an instance of the cipher with stored key, which
        defaults to a randomly generated key."""

    # Note that these are the required methods, but you may define
    # additional methods if you need them.  (I didn't need any.)

    def getKey( self ):
        return self.__key
        """Getter for the stored key."""
        

    def setKey( self, newKey ):
        """Setter for the stored key.  Check that it's a legal
        key."""
        if isLegalKey(newKey) == True:
            self.__key = newKey.lower()
            return self.__key
        elif isLegalKey(newKey) == False:
            return False

    def encryptFile( self, inFile, outFile ):
        """Encrypt the contents of inFile using the stored key
        and write the results into outFile.  Assume inFile exists.
        """
        dictionary = {}
        string = ""
        for i in range(len(LETTERS)):
            dictionary[LETTERS[i]] = self.__key[i]
        inF = open(inFile, "r")
        outF = open(outFile, "w")
        lines = inF.readlines()
        for line in lines:
            for ch in line:
                if ch.isalpha():
                    if ch.isupper():
                        ch = ch.lower()
                        string += dictionary[ch].upper()
                    else:
                        string += dictionary[ch]
                else:
                    string += ch
        outF.write(string)
        inF.close()
        outF.close()
        

    def decryptFile( self, inFile, outFile ):
        dictionary = {}
        string = ""
        for i in range(len(LETTERS)):
            dictionary[self.__key[i]] = LETTERS[i]
        inF = open(inFile, "r")
        outF = open(outFile, "w")
        lines = inF.readlines()
        for line in lines:
            for ch in line:
                if ch.isalpha():
                    if ch.isupper():
                        ch = ch.lower()
                        string += dictionary[ch].upper()
                    else:
                        string += dictionary[ch]
                else:
                    string += ch
        outF.write(string)
        inF.close()
        outF.close()
        

def main():
    subCiph = SubstitutionCipher()
    while True:
        commandStr = input("\nEnter a command (getKey, changeKey, encryptFile, decryptFile, quit): ")
        command = commandStr.strip().lower()
         
        if command == "getkey":
            print("  Current cipher key:", subCiph.getKey())
             
        elif command == "changekey":
            while True:
                inpStr = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
                inp = inpStr.strip().lower()
                if inp == "random":
                    randomStr = makeRandomKey()
                    print("    New cipher key:", randomStr)
                    subCiph.setKey(randomStr)
                    break
                elif isLegalKey(inp) == True:
                    print("    New cipher key:", inp)
                    subCiph.setKey(inp)
                    break
                elif inp == "quit":
                    break
                else:
                    print("    Illegal key entered. Try again!")
                
        elif command == "encryptfile":
            inFilename = input("  Enter a filename: ")

            extension = "-Enc"                  # or "-Dec"
            if inFilename.endswith(".txt"):
                outFilename = inFilename[:-4] + extension + ".txt"
            else:
                outFilename = inFilename + extension

            if os.path.isfile(inFilename) == False:
                print("File does not exist")
            else:
                subCiph.encryptFile(inFilename, outFilename)
                print("The encrypted output filename is:", outFilename)
            
        elif command == "decryptfile":
            inFilename = input("  Enter a filename: ")

            extension = "-Dec"                  # or "-Dec"
            if inFilename.endswith(".txt"):
                outFilename = inFilename[:-4] + extension + ".txt"
            else:
                outFilename = inFilename + extension

            if os.path.isfile(inFilename) == False:
                print("File does not exist")
            else:
                subCiph.decryptFile(inFilename, outFilename)
                print("The decrypted output filename is:", outFilename)

        elif command == "quit":
            print("Thanks for visiting!")
            break

        else:
            print("  Command not recognized. Try again!")
                
main()
