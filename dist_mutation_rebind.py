def add_entry(d):
    d['Mango']=4
def reassign_dict(d):
 d={'Grapes':1,'Apple':2,"Cherry":3,'Guava':5}

dict={'Grapes':1,'Apple':2,"Cherry":3}

print("Before function",dict)

add_entry(dict)
print('After function',dict)

reassign_dict(dict)
print('after function',dict)