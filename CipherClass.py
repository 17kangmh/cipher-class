import random
import os

# A global constant defining the alphabet. 
LETTERS = "abcdefghijklmnopqrstuvwxyz"

def isLegalKey( key ):
    key = key.lower()
    return ( len(key) == 26 and all( [ ch in key for ch in LETTERS ] ) )

def makeRandomKey():
    lst = list( LETTERS )    # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey() ):
        self.__key = key
        """Create an instance of the cipher with stored key, which
        defaults to a randomly generated key."""

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

            extension = "-Enc"                  
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

            extension = "-Dec"                  
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
