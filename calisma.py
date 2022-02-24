import numpy as np

"""arr1 = np.array([21,25,65,78,35,90]).reshape(3,2)
print(arr1)
print("Shape: {}".format(arr1.shape))
print("Number of Elements: {}".format(arr1.size))
print("Dimension: {}".format(arr1.ndim))
print(arr1.dtype)


arr2 = np.random.randint(0,10,size=(3,2))
print("\n" , arr2)
print("Shape: {}".format(arr2.shape))
print("Number of Elements: {}".format(arr2.size))
print("Dimension: {}".format(arr2.ndim))
print(arr2.dtype)

arr3 = np.concatenate([arr1,arr2])
print("\n" , arr3)
print("\n")
print(np.concatenate([arr1,arr2] , axis=0))
print("\n")
print(np.concatenate([arr1,arr2] , axis=1))


arr4 = np.random.normal(50,5,size=(3,2))
print("\n" , arr4)
print("Shape: {}".format(arr4.shape))
print("Number of Elements: {}".format(arr4.size))
print("Dimension: {}".format(arr4.ndim))
print(arr4.dtype)
print(np.sort(arr4))
print("\n")
print(np.sort(arr4 , axis=0))
print("\n")
print(np.sort(arr4 , axis=1))

arr5 = np.linspace(0,20,4).reshape(2,2)
print(arr5)
print("\n")
arr6 = np.linspace(30,60,4).reshape(2,2)
print(arr6)
print("\n")
#print(arr5+arr6)
print("\n")
print(arr5@arr6)
print((arr5@arr6)>400)"""

"""arr6 = np.arange(4,20).reshape(4,4)
print(arr6)

a,b = np.vsplit(arr6,[2])
print("A: {} \n B: {}".format(a,b))
print("C: ",a[::-1])

print("SingleDimension: ",np.ravel(arr6))"""

"""a = np.floor(10*np.random.random((2,3)))
b = np.floor(10*np.random.random((2,3)))
print(a)
print("\n")
print(b)
print("\n")

c = np.vstack((a,b)) 
print(c)
print("\n")

d = np.hstack((a,b)) 
print(d)"""

"""y = np.arange(9,18).reshape(3,3)
print(y)
print("\n")
print(y[1,2])
print(y[:1,-1:])
print(y[1:2,2:3])
print(y[2,[1,2]])"""

"""#10*x0+x1=23
#-1*xo+9*x1 =6

x = np.array([[10,-1],[1,9]])
y = np.array([23,6])

sonuc = np.linalg.solve(x,y)
print("Sonuc: {}".format(sonuc))"""