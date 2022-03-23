list_flat = []
def flat(l):
    for i in l:
        if type(i)==list:
            flat(i)
        else:
            list_flat.append(i)

flat([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(list_flat)
