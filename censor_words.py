# censor.py
#   A program to censor specific words

def readFile(filename):
    infile = open(filename , 'r')
    data = infile.readlines()
    return data

class censor:

    def __init__(self, data):
        self.data = data

    def censorWord(self, words):
        censored = ""
        for line in self.data:
            for word in line.split():
                newWord = self.__censorWord(words, word)
                censored = censored + newWord +  " "
            censored = censored.rstrip()
            censored = censored + "\n"
        return censored
    
    def censor4ch(self):
        censored = ""
        for line in self.data:
            for word in line.split():
                newWord = self.__censor4ch(word)
                censored = censored + newWord +  " "
            censored = censored.rstrip()
            censored = censored + "\n"
        return censored

    def __censor4ch(self, word):
        if len(word) == 4:
            newWord = "****"
        else:
            newWord = word
        return newWord

    def __censorWord(self, words, word):
        if word in words:
            newWord = "*" * len(word)
        else:
            newWord = word
        return newWord
        
def main():
    print("A program to censor specefic words")
    filename = input("Enter the name of the data file: ")
    wordFilename = input("Enter the name of the censored words file: ")
    censor_Words = readFile(wordFilename)
    data = readFile(filename)
    censorData = censor(data)
    censored = censorData.censorWord(censor_Words[0])
    outfilename = input("Enter a name for the output file: ")
    outfile = open(outfilename , 'w')
    #print(censored)
    print(censored, file = outfile)
    input("Press <Enter> to exit")
    
if __name__ == '__main__':
    main()
