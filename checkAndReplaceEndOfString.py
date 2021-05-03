def check_EOString(str):
    if len(str)>2:
        if (str[-3:]!="ing"):
            str+="ing"
        else:
            str+="ly"
    return str