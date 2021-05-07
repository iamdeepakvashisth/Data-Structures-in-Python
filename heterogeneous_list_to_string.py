def heterogeneous_data_to_str(li):
    res=''
    for i in li:
        if type(i)!=str:
            res+=str(i)
        else:
            res+=i
    return res