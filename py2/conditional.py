a=int(input("Enter any no...:"))
if(a%2==0):
    print(a," is even")
else:
    print(a," is odd")



b=int(input("Enter any no:"))
if(b==2 or b==3):
    print(b," is prime")
elif(b==1):
    print(b," is non prime")
elif(b>3):
    c=2
    while(c<=(b**0.5)):
        if(b%c==0):
            print(b," is non prime")
        else:
            print(b," is prime")
        c+=1
else:
    print(b," is non prime")
    


        
