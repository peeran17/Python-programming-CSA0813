#Loops : In Simple Do something again and agian in a sequence
# 1.Loops are used to reperate the task in Multiple Times
#2.it iscommonly Used in range(),list,tuple,string,....

# Syntax : for variable in sequence(Means The declared variable name):             
#             print(variable)

# print 10 Natural Numbers
for i in range(1,11) :
    print(i)

#print Even Numbers
sum=0
for i in range(10):
    if i % 2 == 0:
        print(i)
        sum+=i
        
print("Sum",sum)

# Sum Of N Natural Numbers
N=int(input("enter How Many Natural sum do U Want:"))
sum=0
for i in range(1,N):
    print(i)
    sum +=i
print("Sum Of N Natural Numbers :",sum) 

# Multiplication Table
N=int(input("Enter a Number Which Multiplication Table u want?"))

for i in range(1,11):
    print(i*N)

# Factorial 
N=int(input("enter A Factorial Number :"))
fact=1
for i in range(1,N+1):
    fact*=i
print("Fatorial of",N,"Is",fact)    
           
# reverse Numbers

N=int(input("Enter The N Value:"))

for i in range(N,0,-1):
    print(i)