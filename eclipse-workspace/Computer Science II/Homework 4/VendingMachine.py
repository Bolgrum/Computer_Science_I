# Homework 4.1                      VendingMachine.py
# Version:                          v1.0.1
# Completed by:                     Anthony Braden on 09/24/2021

# 9.16 LAB: Vending Machine
# Given two integers as user inputs that represent the number of 
# drinks to buy and the number of bottles to restock, create a 
# VendingMachine object that performs the following operations:
# 
# Purchases input number of drinks
# Restocks input number of bottles
# Reports inventory
# A VendingMachine's initial inventory is 20 drinks.
#
# Ex: If the input is:
#
# 5
# 2
# the output is:
#
# Inventory: 17 bottles

class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    drink_machine = VendingMachine()
    drinks_to_buy = int(input())
    bottles_to_stock = int(input())
    drink_machine.purchase(drinks_to_buy)
    drink_machine.restock(bottles_to_stock)
    drink_machine.report()