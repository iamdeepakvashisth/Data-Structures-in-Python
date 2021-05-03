def replace_occurrences_firstChar(str, c):
    char=str[0]
    newString=str.replace(char,c)
    newString=str[0]+newString[1:]
    return newString


	