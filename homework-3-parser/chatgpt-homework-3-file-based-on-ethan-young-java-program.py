# Global declarations
# Variables
charClass = None
lexeme = [""] * 100
nextChar = ""
lexLen = 0
token = None
nextToken = None
line = ""
position = 0

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
EOF = -1


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
        nextToken = SUB_OP
    elif ch == "*":
        addChar()
        nextToken = MULT_OP
    elif ch == "/":
        addChar()
        nextToken = DIV_OP
    elif ch == "=":
        addChar()
        nextToken = ASSIGN_OP
    else:
        addChar()
        nextToken = EOF
    return nextToken


def addChar():
    global lexLen
    if lexLen <= 98:
        lexeme[lexLen] = nextChar
        lexLen += 1
        lexeme[lexLen] = "\0"
    else:
        # print("Error - lexeme is too long \n")
        #make the array lexeme bigger
        lexeme.append(nextChar)
        lexeme.append("\0")
        lexLen += 1


def getChar():
    global nextChar, charClass, position
    if position < len(line):
        nextChar = line[position]
        if nextChar.isalpha():
            charClass = LETTER
            position += 1
        elif nextChar.isdigit():
            charClass = DIGIT
            position += 1
        else:
            charClass = UNKNOWN
            position += 1
    else:
        charClass = EOF


def getNonBlank():
    global nextChar
    while nextChar.isspace():
        getChar()


def lex():
    global lexLen, charClass, nextToken, nextChar, position
    for i in range(len(lexeme)):
        lexeme[i] = " "
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
        intStr = "".join(lexeme).strip()
        #replace \x00 with nothing in the string intStr
        intStr = intStr.replace("\x00", "")
        bigInt = int(intStr)
        if bigInt > 2**63 - 1:
            raise ValueError("Value too large")
        if bigInt < -(2**63):
            raise ValueError("Value too small")
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme[0] = "E"
        lexeme[1] = "O"
        lexeme[2] = "F"
    str_lexeme = "".join(lexeme)
    print("Next token is:", nextToken, "Next lexeme is", str_lexeme)

simplefile = "C:\\Users\\peter\\OneDrive - Marshall University\\GitHub\\programming-languages-cs-300\\homework-3-parser\\simple-example-that-works.txt"
longidentifier = "C:\\Users\\peter\\OneDrive - Marshall University\\GitHub\\programming-languages-cs-300\\homework-3-parser\\long-identifier-name.txt"
reallybignumber="C:\\Users\\peter\\OneDrive - Marshall University\\GitHub\\programming-languages-cs-300\\homework-3-parser\\really-big-number.txt"
if __name__ == "__main__":
    # Getting the file and removing the spaces to be able to read the file easier
    with open(reallybignumber, "r") as file:
        line = file.readline().replace(" ", "")
        # print(
        #     line
        # )  # Just printing the line to make sure the analyzer didn't miss something

    getChar()
    while nextToken != EOF:  # Using this to run through till the end of the file
        lex()
