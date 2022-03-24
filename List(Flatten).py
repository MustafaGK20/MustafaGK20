https://app.patika.dev/courses/python-temel/proje

list_flat = []
def flat(l):
    for i in l:
        if type(i)==list:
            flat(i)
        else:
            list_flat.append(i)

flat([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(list_flat)


myList = [[1, 2], [3, 4], [5, 6, 7]]

def Reversing(myList):
    myList.reverse()
    for i in myList:
        i.reverse()
    return myList
print(Reversing(myList))
