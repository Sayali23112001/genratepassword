import string
import random

sizeofpass=int(input("PLZ ENTER SIZE OF PASSWORD "))

print('''Choose set  for password from these:
      A.Letters
      B.Digits
      C.Special Characters
      D.Exit''')

print("PLZ SELECT A TO B TO GENRATE PASSWORD AND D FOR EXECUTION ")

chlist=""

while(True):
    ch=input("PLZ ENTER CHARACTER ")
    if(ch=='A'):
        chlist +=string.ascii_letters
    elif(ch=='B'):
        chlist +=string.digits
    elif(ch=='c'):
        chlist +=string.punctuation
    elif(ch=='D'):
        break
    else:
        print("PLZ SELECT VAILD OPTION ")
password=[]
for i in range(sizeofpass):
    randomch=random.choice(chlist)
    password.append(randomch)
print("THE GENRATED PASSWORD IS" + "".join(password))
