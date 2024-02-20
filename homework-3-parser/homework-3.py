import re
examplestring="result = oldsum-value/100+1-1*1/1+(1+1); \t\r\n\f\v"
whitespacestring=" \t\r\n\f\vword"

string="foo123bar"
print("123" in string)
print(re.search("123", string))
print(re.sub('\s',"",whitespacestring))
print(len(re.sub('\s',"",whitespacestring)))
print(len("word"))
examplestringwithnowhitespacecharacters=re.sub('\s',"",examplestring)
print(examplestringwithnowhitespacecharacters)
print(list(examplestringwithnowhitespacecharacters))
print(re.findall(r"[a-zA-Z][a-zA-Z0-9]*", examplestringwithnowhitespacecharacters))
print(re.findall(r"\+", examplestringwithnowhitespacecharacters))
print(re.findall(r"\-", examplestringwithnowhitespacecharacters))
print(re.findall(r"\*", examplestringwithnowhitespacecharacters))
print(re.findall(r"/", examplestringwithnowhitespacecharacters))
print(re.findall(r"=", examplestringwithnowhitespacecharacters))
print(re.findall(r";", examplestringwithnowhitespacecharacters))
print(re.findall(r"\(", examplestringwithnowhitespacecharacters))
print(re.findall(r"\)", examplestringwithnowhitespacecharacters))
[["result","identifier"],["=","assignment operation"],["oldsum","identifier"],["value","identifier"],["100","number"],["1","number"],["1","number"],["1","number"],["1","number"],["1","number"],["1","number"],["1","number"]]
#here is examplestring for reference again.
#examplestring="result = oldsum-value/100+1-1*1/1+(1+1); \t\r\n\f\v"
# for character in list(examplestringwithnowhitespacecharacters):
#     # if the character is a letter
currentlexeme="none"
lexemearray=[]
lexemestring=""

for character in examplestringwithnowhitespacecharacters:
    if character.isalpha() and currentlexeme=="none":
        currentlexeme="identifier"
        print(currentlexeme)
        print(character)
    if currentlexeme=="identifier" and character.isalnum():
        lexemestring+=character
        print(lexemestring)
    if character=="=" and currentlexeme!="assignment operation":
        lexemestring=""
        lexemestring="="
        currentlexeme="assignment operation"
        print(lexemestring)
        print(currentlexeme)
        
# for character in examplestringwithnowhitespacecharacters:
#     print(character)
simpleexample="1234"
#append $ to simpleexample to make it easier to parse
appendedsimpleexample=simpleexample+"$"
currentlexeme="none"
previouslexeme="none"
# for character in simpleexample:
#     print(character)
#     if character.isalpha() and currentlexeme=="none":
#         currentlexeme="identifier"
#         currentidentifierstring=""
#     if character.isalpha() and currentlexeme=="identifier":
#         currentidentifierstring+=character
#         print(currentidentifierstring)
#     print()
lexemes=[]
for character in appendedsimpleexample:
    print(character)
    if character.isdigit() and currentlexeme=="none":
        currentlexeme="number"
        currentnumberstring=""
    if character.isdigit() and currentlexeme=="number":
        currentnumberstring+=character
        print(currentnumberstring)
        #append to lexemes [currentnumberstring,"number"]
        lexemes.append([currentnumberstring,"number"])
    print(lexemes)
    print()
print(lexemes)