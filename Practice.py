r1=int(input(""))
c1=int(input(""))
r2=int(input(""))
c2=int(input(""))
matrix1=[]
matrix2=[]

if c1!=r2:
    print(" Multiplication not Exist")
print("matrix1:")
for i in range(r1):
    row=[]
    for j in range(c1):
        value=int(input(""))
        row.append(value)
    matrix1.append(row)

for i in range(r2):
    row=[]
    for j in range(c2):
        value=int(input(""))
        row.append(value)
    matrix2.append(row)    
print("Matrix 1 :")            
for i in range(r1):
    for j in range(c1):
        print(matrix1[i][j],end="") 
    print()    
print("Matrix 2:")
for i in range(r2):
    for j in range(c2):
        print(matrix2[i][j],end="") 
    print()

print("Now We are Goin to Addition Of Two Matrices")
result=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(matrix1[i][j]+matrix2[i][j])
    result.append(row) 

for row in result:
    print(row)  

print(" Now We are Multiplication of Two Matrices:")
result1=[]
for i in range(r1):
    row=[]
    for j in range(c2):
        sum=0
        for k in (c1):
            sum+=matrix1[i][k]*matrix2[k][j]
        row.append(sum)
    result1.append(row)   
for row in result1:
    print(row)      


#PASCASLS TRIANGLE
n=int(input("Enter Number Of Rows:")) 
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    num=1
    for j in range(1,i+1):
        print(num,end="")
        num=num*(i-j) // j
    print()        


# Hallow Sphere
n=int(input("Enter number of rows:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(' ',end="")
    print()            


n=int(input("Enter Number of Rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()   
for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()                 

print("Enter -1 It will Exit ...")

pos_sum=0
pos_count=0
neg_sum=0
neg_count=0

while True:
    n=int(input(" Enter The N Values :"))

    if n == -1:
        break
    elif n>0:
        pos_sum+=n
        pos_count+=1
    else:
        neg_sum+=n
        neg_count+=1
if pos_count>0:
    pos_avg= pos_sum // pos_count     
    print(f'The Positive Avg Sum={pos_avg}')   
else:
    print("No Negative Avg ")

if neg_count>0:
    neg_avg= neg_sum //  neg_count
    print(f"The Avg Negative Avg={neg_avg}")    
else:
    print("No Negative Sum ")    







list=[8,4,5,3,6,9]
list.sort(reverse=True)
list=[0,1,2,3,4,5,6]
print(list[0:4])


print(" Welcome to our Student Attendance Caluclator !..")

tca=int(input("Total Number of Clasees :"))
nca=int(input("Enter Number of Classes Attended:"))

Attendance= (nca/tca)*100

if Attendance >= 75:
    print(f'Student {Attendance} is Eligible for Exam..')
else:
    print(" Student {Attendance} is Not Eligible !")


username = 'peeran@24'
password = 7886
attempts = 3

while attempts > 0:
    name = input("Enter your username: ")   # First ask for username
    passs = int(input("Enter your Password: "))  # Then ask for password

    if username == name and password == passs:
        print(" Login Successfully ..")
        break   # stop loop if login correct
    else:
        attempts -= 1
        if attempts > 0:
            print(f" Invalid! You have {attempts} attempt(s) left.")
        else:
            print(" Account Blocked! Too Many Attempts.")

    




pin=516502
amount=5000
x=int(input("Enter PIN"))
if pin == x:
    m=int(input("Enter Withddrawl Amount"))
    if amount<m:
        print("in Sufficint Balance !")
    else:
        print("Successfully Transtracted...") 
        print("Available Balance is ..",amount-m)
else:
    print("Entered Wrong pin..!")      

m=int(input("Enter your Marks :"))
if(m>=90):
    print('A')
elif m>=80:
    print('B')
elif m>=60:
    print('C')
else:
    print("FAIL !")   


n=int(input("enter  a Numkber :"))
q=0
while(n>0):
    p=n%10
    q=q+p
    n=n // 10
print("sum of the individul Digits",q )    


 



          
        


