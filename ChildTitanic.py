import pandas as pd
import numpy as np
import seaborn as sns

data_Titanic = sns.load_dataset("titanic")
#print(data_Titanic.columns)
#print(data_Titanic.head())

data_child = data_Titanic[data_Titanic.who == "child"]
#print(data_child.tail())
childTotal = data_child["who"].count()
#print("ChildTotal:",childTotal)

data_man = data_Titanic[data_Titanic.who == "man"]
#print(data_man.head())
manTotal = data_man["who"].count()
#print("ManTotal: {}".format(manTotal))

data_woman = data_Titanic[data_Titanic.who == "woman"]
#print(data_woman)
womanTotal = data_woman["who"].count()
#print("WomanTotal: {}".format(womanTotal))

data_female = data_Titanic[data_Titanic.sex == "female"]
#print(data_female)
femaleTotal = data_female["sex"].count()
#print("FemaleTotal: ",femaleTotal)

girlChild = femaleTotal-womanTotal
#print("GirlChild: ",(girlChild))

boyChild = childTotal-(femaleTotal-womanTotal)
#print("BoyChild: ",boyChild)

aliveChild = list(data_child["alive"]=="yes").count(True)
#print("Alive_Child_Total: ",aliveChild)
deadChild = childTotal-aliveChild
#print("Dead_Child_Total: ",deadChild)

#print(set(data_child["embark_town"])) #{'Queenstown', 'Cherbourg', 'Southampton'}
queenstown = list((data_child["embark_town"]=="Queenstown")).count(True)
cherbourg =  list((data_child["embark_town"]=="Cherbourg")).count(True)
southampton = list((data_child["embark_town"]=="Southampton")).count(True)
#print("Queenstown: {} \nCherbourg: {} \nSouthampton: {}".format(queenstown,cherbourg,southampton))

alive_Child_Southampton = list((data_child["alive"] =="yes" )&( data_child["embark_town"] == "Southampton")).count(True)
#print("Alive_Child_Southampton: {} \nDead_Child_Southampton: {}".format(alive_Child_Southampton,(southampton-alive_Child_Southampton)))
alive_Child_Queenstown = list((data_child["alive"] =="yes" )&( data_child["embark_town"] == "Queenstown")).count(True)
#print("Alive_Child_Queenstown: {} \nDead_Child_Queenstown: {}".format(alive_Child_Queenstown,(queenstown-alive_Child_Queenstown)))
alive_Child_Cherbourg = list((data_child["alive"] =="yes" )&( data_child["embark_town"] == "Cherbourg")).count(True)
#print("Alive_Child_Cherbourg: {} \nDead_Child_Cherbourg: {}".format(alive_Child_Cherbourg,(cherbourg-alive_Child_Cherbourg)))

first_Class = list((data_child["class"] == "First")).count(True)
second_Class = list((data_child["class"] == "Second")).count(True)
third_Class = list((data_child["class"] == "Third")).count(True)
#print("First_Class_Child: {} \nSecond_Class_Child: {} \nThird_Class_Child: {}".format(first_Class,second_Class,third_Class))

first_Southampton = list((data_child["class"]=="First") & (data_child["embark_town"]=="Southampton")).count(True)
second_Southampton = list((data_child["class"]=="Second") & (data_child["embark_town"]=="Southampton")).count(True)
third_Southampton = list((data_child["class"]=="Third") & (data_child["embark_town"]=="Southampton")).count(True)
#print("First_Southampton: {} \nSecond_Southampton: {} \nThird_Southampton: {}".format(first_Southampton,second_Southampton,third_Southampton))

first_Queenstown = list((data_child["class"]=="First") & (data_child["embark_town"]=="Queenstown")).count(True)
second_Queenstown = list((data_child["class"]=="Second") & (data_child["embark_town"]=="Queenstown")).count(True)
third_Queenstown = list((data_child["class"]=="Third") & (data_child["embark_town"]=="Queenstown")).count(True)
#print("First_Southampton: {} \nSecond_Southampton: {} \nThird_Southampton: {}".format(first_Queenstown,second_Queenstown,third_Queenstown))

first_Cherbourg = list((data_child["class"]=="First") & (data_child["embark_town"]=="Cherbourg")).count(True)
second_Cherbourg = list((data_child["class"]=="Second") & (data_child["embark_town"]=="Cherbourg")).count(True)
third_Cherbourg = list((data_child["class"]=="Third") & (data_child["embark_town"]=="Cherbourg")).count(True)
#print("First_Southampton: {} \nSecond_Southampton: {} \nThird_Southampton: {}".format(first_Cherbourg,second_Cherbourg,third_Cherbourg))


class_Child = [(first_Class,first_Southampton,first_Queenstown,first_Cherbourg),
               (second_Class,second_Southampton,second_Queenstown,second_Cherbourg),
               (third_Class,third_Southampton,third_Queenstown,third_Cherbourg)]
dfClass_Child = pd.DataFrame(class_Child, columns=["Child","Southampton","Queenstown","Cherbourg"], index=["First","Second","Third"])
#print(dfClass_Child)


embark_Town = [(childTotal,southampton,queenstown,cherbourg),
               (aliveChild,alive_Child_Southampton,alive_Child_Queenstown,alive_Child_Cherbourg),
              (deadChild,(southampton-alive_Child_Southampton),(queenstown-alive_Child_Queenstown),(cherbourg-alive_Child_Cherbourg))]
dfEmbark_Town = pd.DataFrame(embark_Town, columns=["Child","Southampton","Queenstown","Cherbourg"] , index=["Total","Alive","Dead"])
#print(dfEmbark_Town)

fare_Total = np.sum(data_child["fare"])
first_Fare_total = np.sum((data_child[(data_child["class"]=="First")])["fare"])
second_Fare_total = np.sum((data_child[(data_child["class"]=="Second")])["fare"])
third_Fare_total = np.sum((data_child[(data_child["class"]=="Third")])["fare"])
alive_Fare_total = np.sum((data_child[(data_child["alive"]=="yes")])["fare"])
dead_Fare_total = np.sum((data_child[(data_child["alive"]=="no")])["fare"])

#print("Fare_Total: {} \nAlive_Fare_total: {} \nDead_Fare_total: {} \nFirst_Fare_Total: {} \nSecond_Fare_Total: {} \nThird_Fare_Total: {}".format(fare_Total,alive_Fare_total,dead_Fare_total,first_Fare_total,second_Fare_total,third_Fare_total))

list_Fare = [fare_Total,alive_Fare_total,dead_Fare_total,first_Fare_total,second_Fare_total,third_Fare_total]
df_Fare = pd.DataFrame(list_Fare, columns=["Fare"], index=["Total","Alive","Dead","First","Second","Third"])
#print(df_Fare)

df_town_class = pd.concat([dfEmbark_Town,dfClass_Child], axis=0)
#print(df_town_class)

df_town_class_fare = pd.concat([df_town_class,df_Fare], axis=1)
print(df_town_class_fare)
print("\n")
print(df_town_class_fare.describe())
print("\n")
print(data_child.describe())
print("\n")
print(data_Titanic.describe())