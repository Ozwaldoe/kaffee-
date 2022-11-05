import time
import os
from dhooks import Webhook, File
from io import BytesIO
import shutil

list = []
webhook = Webhook('https://discord.com/api/webhooks/1026256179640414319/9bQ1wwtmL7d3hAEuFNk-brrQnTF8B5oYZRK9IzHNGLM4pAISB4ihoh1mZbLCPzzabCaN')

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
coffee = "coffee"
tea = "tea"
HC = "hot chocolate"

#prices
order = input()
if order == "coffee":
    price = int("5")
elif order == "tea":
    price = int("3")
elif order == f"{HC}": #fuck you im not typing out hot chocolate again 
    price = int("9")
else: 
    print("we dont serve that")
    exit()

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
        print(f"\nPlease hand £{amount} to Auzie when you next see him")
    elif input == "paypal":
        print(f"\nPlease paypal Auzie £{amount} as soon as possible")   
        break
    else: 
        print("\nsorry, we dont accept that (or you spelt it wrong). I guess you get it for free because im too lazy to code a way to ask again.")

#make list contain name + order + price
list.append(f"name: {name} | order: {order} | {order}'s ordered: {order_amount} | amount owed: £{amount}")

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

time.sleep(5)
print('bye')
exit()




