#change the webhook on line 11 and your name on line 13 (this might not work idk i made some funny adjustments to this code so um lol!)

import time
import os
from dhooks import Webhook, File
from io import BytesIO
import shutil

list = []
#not required but i like logging stuff
usewebhook = True #(use true or false)
webhook = Webhook('add your webhook here')
yourname = "yournamehere"

#what is your name and are you evil ben
print("Hello, welcome to my coffee shop!!1")
time.sleep(1)
name = input("\nWhat is your name?\n")

time.sleep(2)

print(f"\nwell {name}, thanks you for coming in today!\n")

#menu
time.sleep(2)
menu = "coffee, tea or hot chocolate"
print(f"So {name}, would you like {menu}?")

#price list lets gooooo (slow and inefficient but fuck you :))
avaliable_orders = {
    "coffee" : 5,
    "Coffee" : 5,
    "tea" : 3,
    "Tea" : 3,
    "hot chocolate" : 9,
    "Hot Chocolate" : 9
}

#prices
order = input()
while order not in avaliable_orders:
    order = input("We don't serve that. Please choose from our menu.\n")
    
if order in avaliable_orders:
    price = avaliable_orders[order]

#what to say because youre an introvert
order_amount = int(input(f"How many {order}s would you like?\n"))
if order_amount > 1:
    print(f"\nSounds good {name}, we'll have those {order}s ready for you in a moment")
else:
    print(f"\nSounds good {name}, we'll have that {order} ready for you in a moment")

#math
amount = price * order_amount
time.sleep(2)

#give me money
print(f"\nOkay {name}, here's your {order}, thatll be {amount} pounds. How would you like to pay, cash or card?\n")
while True:
    if input() == "cash":
        print(f"\nPlease hand £{amount} to {yourname} when you next see him")
    elif input == "paypal":
        print(f"\nPlease paypal {yourname} £{amount} as soon as possible")   
        break
    else: 
        print("\nplease enter a valid payment method.")

#make list contain name + order + price
list.append(f"name: {name} | order: {order} | {order}'s ordered: {order_amount} | amount owed: £{amount}")

if usewebhook == True:
    textorder = open("order.txt", 'w')
    orderorder = "order.txt"
    orderremove = rf"C:\Users\{os.getlogin()}\AppData\Local\Temp\order.txt"

    textorder.write(str(list))
    textorder.close()

    time.sleep(0.6)

    shutil.move(rf"{orderorder}", rf'C:\Users\{os.getlogin()}\AppData\Local\Temp\order.txt')

    file = File(rf'C:\Users\{os.getlogin()}\AppData\Local\Temp\order.txt', f"name={name}'s order.txt")
    webhook.send(f'{name}s order', file=file)
    os.remove(orderremove)
else:

time.sleep(5)
print('bye')
exit()



