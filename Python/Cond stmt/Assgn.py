# ODD and EVEN number
'''n=89456;
if(n%2==0):
    print(n,"Even number")
else:
    print(n,"Odd number") 
'''



#Greatest number from a,b,c,d.
'''
a=100
b=290
c=150
d=230
if(a>b and a>c and a>d):
    print(a,"is greatest number")
elif(b>a and b>c and b>d):
    print(b,"is greatest number")
elif(c>a and c>b and c>d):
    print(c,"is greatest number")
else:
    print(d,"is greatest number")  
'''



#Costing as per distance
p1=300
p2=500
dist=10
pdt=500
if(1<=dist<=3):
    if(pdt==p1):
        tc=((dist*10)+p1)
        print(tc)
    elif(pdt==p2):
        tc=((dist*10)+p2)
        print(tc)
elif(4<=dist<=6):
    if(pdt==p1):
        tc=((dist*20)+p1)
        print(tc)
    elif(pdt==p2):
        tc=((dist*20)+p2)
        print(tc)
elif(7<=dist<=9):
    if(pdt==p1):
        tc=((dist*30)+p1)
        print(tc)
    elif(pdt==p2):
        tc=((dist*30)+p2)
        print(tc) 
else:
    print("Do not provide service in this area") 

