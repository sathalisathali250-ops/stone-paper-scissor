from random import*
st=["stone","paper","scissor"]
print("THE OPTION YOU HAVE TO CHOOOSE:",st)
last=int(input("How many you want to play:"))
ch=1
sc=0
sys=0

while ch<=last:
    user=input("User choice:")
    comp=choice(st)
    print("Computer Choice:",comp)
    if user==comp:
        sc+=0
        sys+=0
    elif user=="stone":
        if comp=="scissor":
            sc+=1
        else:
            sys+=1
    elif user=='paper':
        if comp=='stone':
            sc+=1
        else:
            sys+=1
    elif user=='scissor':
        if comp=='paper':
            sc+=1
        else:
            sys+=1
    ch+=1
print("Computer score:",sys)
print("user score:",sc)

if sys==sc:
    print("Score Level")
elif sys>sc:
    print("Computer won")
else:
    print("User won")
