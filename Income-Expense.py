print("-------End Of The Month-------")

print("***********INCOME***********")

x = int(input("Enter the number of creditors: "))
counter_income = 1
total_income = 0

while counter_income <= x:
    counter_income = counter_income+1
    FirstName = input("Firstname: ")
    LastName = input("Lastname: ")
    Amount = int(input("Amount: "))
    Tel_No = input("Tel No: ")
    print(FirstName.capitalize(), LastName.capitalize(),": ",Amount,"TL ","Telephone Number: {}".format(Tel_No))

    total_income = total_income + Amount

print("Total Income: ", total_income)

print("***********EXPENSE***********")

y = int(input("Enter the number of creditors: "))
counter_expence = 1
total_expence = 0

while counter_expence<= x:
    counter_expence = counter_expence+1
    FirstName = input("Firstname: ")
    LastName = input("Lastname: ")
    Amount = int(input("Amount: "))
    Tel_No = input("Tel No: ")
    print(FirstName.capitalize(), LastName.capitalize(),": ",Amount,"TL ","Telephone Number: {}".format(Tel_No))

    total_expence = total_expence + Amount

print("Total Expence: ", total_expence)

money_case = total_income - total_expence
#print("Money Case: ",money_case)

if money_case > 0:
    print("{} Kardayız.".format(money_case))
elif money_case == 0:
    print("Elde var koca bir {}.".format(money_case))
else:
    print("{} zarardayız!!!".format(money_case))