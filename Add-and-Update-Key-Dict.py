import operator
dic={'1':'Rahul','3':'Jai','2':'Zara','5':'Robert'}
#Adding a key to a dict
dic['6']="Simran"
#updating existing key in a dict
dic['6']='Kajal'
print('Sorted in Ascending order of values: ', end=" ")
print(sorted(dic.items(), key=operator.itemgetter(1),))
print('Sorted in Descending order of values: ', end=" ")
print(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))