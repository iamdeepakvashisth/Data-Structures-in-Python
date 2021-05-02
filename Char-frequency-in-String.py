#Number of characters (character frequency) in a string
a="ddddddddsldjwlkkkkkdjwqdw"

def char_frequency(string_data):
    d=dict()
    for char  in string_data:
        if char not in d:
            d[char]=1
        else:
            d[char]+=1
    return d

char_frequency(a)