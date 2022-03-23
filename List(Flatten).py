list_flat = []
def flat(l):
    for i in l:
        if type(i)==list:
            flat(i)
        else:
            list_flat.append(i)

flat([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(list_flat)

#############################################

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list_flat = []
for i in range(len(liste)):
    try:
        for j in range(len(liste[i])):
            list_flat.append(liste[i][j])
    except TypeError:
        list_flat.append(liste[i])

list_flat2 = []
for i in range(len(list_flat)):
    try:
        if type(list_flat[i])==list:
            for j in range(len(list_flat[i])):
                list_flat2.append(list_flat[i][j])
        else:
            list_flat2.append(list_flat[i])
    except TypeError:
        list_flat2.append(list_flat[i])

list_flat3 = []
for i in range(len(list_flat2)):
    if type(list_flat2[i]) == list :
        for j in range(len(list_flat2[i])):
            list_flat3.append(list_flat2[i][j])
    else:
        list_flat3.append(list_flat2[i])
print(list_flat3)
