#1.Odd nr from 1-50 and also count of that nr.:
'''
for i in range(50):
    if(i%2!=0):
        print(i)
'''

#2.Prime nr or not:-------------------------------------------------------------------
'''
n=10
flag=0
for i in range(2,n+1):
    if(n%i==0):
        flag==1
                
if(flag==1):
    print(n,"Prime number")
else:
    print(n,"Not-prime number")
    '''

#3.table of 3:
'''
n=3
for i in range(1,11):
    #print(n,"*",i,"=",n*i)
    print(n*i)
    '''
    
#4.Factorial of given nr.:
'''
n=6
f=1
for i in range(1,n+1):
    f=f*i
print("Factorial of",n,"is",f)
'''

#5.Reverse nr.:-------------------------------------------------------------------
'''
n="1456"
for i in range(1,5)
    print(n[i])
'''

#6.Print series x^1+x^2+x^3+--x^n, sum of series:
#print( pow(3,4) )
'''
x=3
n=8
sum=0
for i in range(1,n+1):
    a=(pow(x,i))
    sum=sum+a
    print(a)
print("sum=",sum)
'''

#7.1,12,123,1234 in single line one by one:
'''
n=10
for i in range(n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''
   
#8.1,22,333,444 in single line one by one:
'''
n=7
for i in range(n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
'''

#9.54321,4321,321,21,1 in single line one by one:
'''
n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
'''

#10.1,10,101,1010,10101 in single line one by  one:
'''
n=4
for i in range(n+1):
    for j in range(1,i+1):
        if(j%2==0):
            print(0,end="")
        else:
            print(1,end="")
    print()
'''           
    
    
#11.1,13,135,1357 in single line one by  one:
'''
n=6
for i in range(n+1):
    for j in range(1,i+1):
        print(2*j-1,end="")
    print() 
''' 

   
#12.*****,****,***,**,* in single line one by one:--------------------------------------------
'''
n=5
for i in range(5,0,-1):
    for k in range(0,n,1):
        print(" ",end="")
       
    for j in range(i,0,-1):
        print("*",end="")
    print()
'''

#13.*,***,*****,*******,*****,***,* in single line one by one:



   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    