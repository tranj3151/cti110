#Jade Tran
#11/16/24
#P5LAB
#Disperse change code

import random

def disperse_change(change):
    
    cents = round(change * 100)

    dollars = cents // 100
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents

    print(f"Change owed: ${change:.2f}")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    amount_paid = float(input(f"The total owed is ${total_owed}. How much will you pay? $"))
    
    if amount_paid >= total_owed:
        disperse_change(amount_paid - total_owed)
    else:
        print("Insufficient funds.")
        
if __name__ == "__main__":
    main()
