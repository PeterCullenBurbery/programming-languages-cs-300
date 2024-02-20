import os

# Global declarations
# Variables
charClass = None
lexeme = [""] * 100
print(lexeme)
nextChar = ""
lexLen = 0
token = None
nextToken = None
in_fp = None

# Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99

# Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26


# Function declarations
def addChar():
    global lexLen
    if lexLen <= 98:
        lexeme[lexLen] = nextChar
        lexLen += 1
        lexeme[lexLen] = "\0"
    else:
        print("Error - lexeme is too long \n")


def getChar():
    global nextChar, charClass
    nextChar = in_fp.read(1)
    if nextChar != "":
        if nextChar.isalpha():
            charClass = LETTER
        elif nextChar.isdigit():
            charClass = DIGIT
        else:
            charClass = UNKNOWN
    else:
        charClass = -1  # End of file


def getNonBlank():
    global nextChar
    while nextChar.isspace():
        getChar()


def lookup(ch):
    global nextToken
    if ch == "(":
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ")":
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == "+":
        addChar()
        nextToken = ADD_OP
    elif ch == "-":
        addChar()
        nextToken = SUB_OP
    elif ch == "*":
        addChar()
        nextToken = MULT_OP
    elif ch == "/":
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = -1  # End of file
    return nextToken


def lex():
    global lexLen, charClass, nextToken, nextChar
    lexLen = 0
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()
        while charClass == LETTER or charClass == DIGIT:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == -1:
        nextToken = -1  # End of file
        lexeme[0] = "E"
        lexeme[1] = "O"
        lexeme[2] = "F"
        lexeme[3] = "\0"
    print("Next token is:", nextToken, ", Next lexeme is", "".join(lexeme))
    return nextToken


# main driver
if __name__ == "__main__":
    # Open the input data file and process its contents
    file_path = "C:/Users/peter/OneDrive - Marshall University/Documents/spring-2024/cs-300-201/class-lectures/front.in"
    if os.path.exists(file_path):
        in_fp = open(file_path, "r")
        getChar()
        while nextToken != -1:
            lex()
    else:
        print("ERROR - cannot open front.in")
