def merge_strings(str1, str2):
    newStr1=str2[:2] + str1[2:]
    newStr2=str1[:2] + str2[2:]
    final_str= newStr1 + ' ' + newStr2
    return final_str
    