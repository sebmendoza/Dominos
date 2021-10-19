# Name; get_me_pizza.py
# Date: Sept. 11, 2021
# Author: Sebastian Mendoza
# Description: This script will order me pizza.
# Inspiration: Jarvis https://www.youtube.com/watch?v=Nxu6GlDleqA
#               Tech w/ Tim https://www.youtube.com/watch?v=J_ud6KxX_s0\

import sys
from pizzapy import *
import os
from dotenv import load_dotenv

# create func. where user can search menu, better then hard inputting
# if you want pizza, just search pizza, it will not recognize "Bacon Pizza", in future I should see if I can fix this

def search_menu(menu):
    print("You can search the menu!")
    # this input strips leading and trailing whitespace and changes to all lowercase
    item = input("Type an input to look for: ").strip().lower()

    # API needs the first letter to be capitalized to search properly
    if len(item) > 1:
        item = item[0].upper() + item[1:]
        print(f"Results for: {item}")
        menu.search(Name=item)
        print()
    else:
        print("No Results")

# console UI for people to find items to order
def add_to_order(order):
    print("Please type the Codes of the items you'd like to order.")
    print("Hit ENTER to complete your order.")
    while True:
        item = input("Code: ").upper()
        try:
            order.add_item(item)
        except:
            if  item  == '':
                break
            print("Invalid Code")


# loa# d_dotenv()
# # Credit Card Variables
# card_num = os.getenv('card_num')
# ccv = os.getenv('ccv')
# exp = os.getenv('exp')

# change this for wherever you live
TaxRate = 1.13

# Making our 'Customer'
# f_name = os.getenv('f_name')
# l_name = os.getenv('l_name')
# email = os.getenv('email')
# phone_num = os.getenv('phone_num')
# addy = os.getenv('addy')
customer = ConsoleInput.get_new_customer()

# creating variable of the closest location
my_local_dominoes = StoreLocator.find_closest_store_to_customer(customer)
print("Closest Store:")
print(my_local_dominoes)

ans = input({"Would you like to order from this store (Y/N)?"})
if ans.lower in ['yes', 'y']:
    print("Exiting Program...")
    quit()

print("\n------------MENU------------\n")

menu = my_local_dominoes.get_menu()
order = Order.begin_customer_order(customer, my_local_dominoes, "ca")

while True:
    search_menu(menu)
    add_to_order(order)
    answer = input("Would you like to add more items (yes/no)? ")
    if answer.lower() not in 'yes':
        break

total = 0
print("\nYour order is:")
for item in order.data['Products']:
    total += float(item["Price"])
    print(item["Name"] + " $" + item["Price"])
total *= 1.13
total = "{:,.2f}".format(total)
print(f"\nYour total comes to ${total}")

payment = input("\nWill you be paying with Cash or Credit Card? (Cash, Credit Card)")
print(payment)
if payment.lower() in ('card', 'credit card'):
    card = ConsoleInput.get_credit_card()
else:
    card = False

final_dec = input("Would you like to place this order (Y/N)?")
if final_dec.lower() in ['yes', 'y']:
    order.place(card)
    my_local_dominoes.place_order(order, card)
    print("Order Placed!")
else:
    print("Okay, try again next time.")
