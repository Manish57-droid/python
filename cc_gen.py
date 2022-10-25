import random

print("-"*60)
print("  /$$$$$$   /$$$$$$         /$$$$$$  /$$$$$$$$ /$$   /$$")
print(" /$$__  $$ /$$__  $$       /$$__  $$| $$_____/| $$$ | $$")
print("| $$  \__/| $$  \__/      | $$  \__/| $$      | $$$$| $$")
print("| $$      | $$            | $$ /$$$$| $$$$$   | $$ $$ $$")
print("| $$      | $$            | $$|_  $$| $$__/   | $$  $$$$")
print("| $$    $$| $$    $$      | $$  \ $$| $$      | $$\  $$$")
print("|  $$$$$$/|  $$$$$$/      |  $$$$$$/| $$$$$$$$| $$ \  $$")
print(" \______/  \______/        \______/ |________/|__/  \__/")
print(" -------------Tool by HAXORLEET-------------------------  ")

print("\n","                                                    " )

V = int(input("How many Visa cards you want to generate = "))
if V <0:
  print("\n","Error : Visa Value cannot be negative",)

M = int(input("\n How many Master Cards you want to generate = "))
if M <0:
  print("\n","Error : Mastercard Value cannot be negative")

 

visa = ['4' + str(random.randint(111111111111, 999999999999)) for _ in range(V)]
master = ['5' + str(random.randint(111111111111, 999999999999)) for _ in range(M)]

print("\n ","-"*15)
print("   Visa Cards")
print(" ","-"*15)




for i in visa:
   print(" ",i)

print("\n ","-"*15)
print("   Master Cards")
print(" ","-"*15)

for j in master:
    print(" ",j)

print("\n","Thanks for using this tool")    
