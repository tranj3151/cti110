#Jade Tran
#11/2/24
#P4LAB2

while True:
    num = int(input("Enter an integer: "))

    if num <= -1:
        print("This program does not handle negative numbers.")
    else:
        i = 1
        while i <= 5:
            print(f"{num} x {i} = {num * i}")
            i += 1
        for i in range(6, 13):
            print(f"{num} x {i} = {num * i}")

    repeat = input("Would you like to run the program again? (yes/no): ")
    if repeat != 'yes':
        print("Exiting program...")
        break
