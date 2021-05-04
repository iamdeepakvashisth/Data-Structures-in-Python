def longWordWithLength(li):
    dic={}
    for i in li:
        if i not in dic:
            dic[i]=len(i)
    for key, value in dic.items():
        if value==max(dic.values()):
            print(f"Longest word is '{key}' and its length is {value}")