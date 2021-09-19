#1.Odd nr from 1-50 and also count of that nr.:
'''
n=50
count=0
for i in range(n):
    if(i%2!=0):
        count=count+1
        print(i)
print("Total nr of odd nr from 1 to",n," are",count)
''' 


#2.Prime nr or not:
'''
n=53
flag=0
for i in range(2,n):
    if(n%i==0):
        flag=1
                
if(flag==0):
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

#5.Reverse nr.:
'''
n=123456789
rev=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(rev)
'''

#6.Print series x^1+x^2+x^3+--x^n, sum of series:-----------------------------------------
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
for i in range(n):
    for k in range(0,i,+1):
        print(" ",end="")
       
    for j in range(n,i,-1):
        print("*",end="")
    print()
'''

#13.*,***,*****,*******,*****,***,* in single line one by one:
'''
for i in range(1,5):
    for k in range(4,i,-1):
        print(" ", end="")
    for j in range(1,i*2):
        print("*", end="")
    print()
for i in range(3):
    for k in range(0,i+1):
        print(" ",end="")
    for j in range(5,2*i,-1):
        print("*",end="")
    print()
 '''   
    
#14.all prime nr from 1 to 50----------------------------------------------------------------------
'''
flag=0
for i in range(2,50):
    flag=0
    for j in range(2,i+1):
        if(i%j==0):
            flag=1
         
    if(flag==0):
        print(i)
'''        


#15.Given nr is perfect or not:
'''
n=28
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
#print(sum)
if(sum==n):
    print(n,"is perfect number")
else:
    print(n,"is not perfect number")
'''

#16.Given nr is palindrome or not-palindrome number:
'''
n=1849481
rev=0
temp=n
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10 
#print(rev)    
if(temp==rev):
    print(rev,"is palindrome number")
else:
    print(rev,"is not palindrome number")
'''

#17.Fibonicci series
f=0
s=1
for i in range(5):
    t=f+s
    f=s
    s=t
    print(s)
