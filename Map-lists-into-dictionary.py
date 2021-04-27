#Map 2 lists to a dictionary
keys = ['Red', 'Green', 'Blue']
values = ['#AAAAA','#BBBBBB', '#CCCC']
def map_two_lists_into_dictionary(list1, list2):
    return dict(zip(list1, list2))

print(map_two_lists_into_dictionary(keys, values))


#Map 2 lists to a dictionary
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
def map_two_lists(list1, list2):
    d={}
    for i in range(len(keys)):
        d[keys[i]]=values[i]
    return d
print(map_two_lists(keys, values))