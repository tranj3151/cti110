#Jade Tran
#10/19/24
#P3LAB
#This program allows the user to enter a money (float) value with two places after the decimal.

money = float(input("Enter the amount of money as a float: "))
cents = round(money * 100)
dollars = cents // 100
cents = cents % 100
quarters = cents // 25
cents = cents % 25
dimes = cents // 10
cents = cents % 10
nickels = cents // 5
cents = cents % 5
pennies = cents

if dollars > 0:
    print(dollars, "Dollars")
if quarters > 0:
    print(quarters, "Quarters")
if dimes > 0:
    print(dimes, "Dimes")
if nickels > 0:
    print(nickels, "Nickels")
if pennies > 0:
    print(pennies, "Pennies")
if money == 0:
    print("No change")
