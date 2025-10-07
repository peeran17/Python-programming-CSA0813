# User input matrix
r = int(input("Enter Number of Rows: "))
c = int(input("Enter Number of Columns: "))
matrix = []

for i in range(r):
    row=[]
    for j in range(c):
        value=int(input( ))
        row.append(value)
    matrix.append(row)
print("The Matrix")  

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()   
# By take input As Manually
matrix=[ [1,2,3],
         [4,5,6],
         [7,8,9]]  

for row in matrix:
    for val in row:
        print(val,end=" ") 
    print()  \


# Addition And Substraction of Two Matrices

r1=int(input("Enter Number of rows of 1st matrix"))    
c1=int(input("Enter Number of column of 1st matrix"))    
r2=int(input("Enter Number of rows of 2nd matrix"))    
c2=int(input("Enter Number of rows of 2nd matrix"))  

matrix1=[]
matrix2=[]

for i in range(r1):
    row1=[]
    for j in range(c1):
        values=int(input(f" Enter values of 1st Matrix [{i}][{j}]"))
        row1.append(values)
    matrix1.append(row1)  
for i in range(r2):
    row2=[]
    for j in range(c2):
        values=int(input(f"enter values in 2nd matrix[{i}][{j}]"))
        row2.append(values)
    matrix2.append(row2) 

print("Addition and Substraction of Two Matrices")
result1=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(matrix1[i][j]+matrix2[i][j])
    result1.append(row)

for row in result1:
    print(row)  
print()         

print("Substraction")
result2=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(matrix1[i][j]-matrix2[i][j])
    result2.append(row)  

for row in result2:
    print(row)

# Multiplication of Matrices 
r1=int(input("Enter Number of rows of 1st matrix"))    
c1=int(input("Enter Number of column of 1st matrix"))    
r2=int(input("Enter Number of rows of 2nd matrix"))    
c2=int(input("Enter Number of rows of 2nd matrix"))  

matrix1=[]
matrix2=[]

if c1!=r2:
    print("Mulitplication is not possible :")
    exit()

for i in range(r1):
    row=[]
    for j in range(c1):
        value=int(input(""))
        row.append(value)
    matrix1.append(row) 

for j in range(r2):
    row=[]
    for j in range(c2):
        value=int(input(""))
        row.append(value)
    matrix2.append(row) 

# initialize resultant matrix
result=[[0 for _ in range(c2)] for _ in range(r1)]

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j]+=(matrix1[i][k]*matrix2[k][j])
print("Matrix Multiplicationn result") 

for row in result:
    print(row)



# Multiplication  of 3 matrices
# Input dimensions for 3 matrices
r1 = int(input("Enter number of rows for Matrix A: "))
c1 = int(input("Enter number of columns for Matrix A: "))

r2 = int(input("Enter number of rows for Matrix B: "))
c2 = int(input("Enter number of columns for Matrix B: "))

r3 = int(input("Enter number of rows for Matrix C: "))
c3 = int(input("Enter number of columns for Matrix C: "))

# Check if multiplication is possible: c1 == r2 and c2 == r3
if c1 != r2 or c2 != r3:
    print("Matrix multiplication not possible with these dimensions!")
    exit()

# Input Matrix A
print("Enter elements of Matrix A:")
A = []
for i in range(r1):
    row = []
    for j in range(c1):
        val = int(input(f"A[{i}][{j}]: "))
        row.append(val)
    A.append(row)

# Input Matrix B
print("Enter elements of Matrix B:")
B = []
for i in range(r2):
    row = []
    for j in range(c2):
        val = int(input(f"B[{i}][{j}]: "))
        row.append(val)
    B.append(row)

# Input Matrix C
print("Enter elements of Matrix C:")
C = []
for i in range(r3):
    row = []
    for j in range(c3):
        val = int(input(f"C[{i}][{j}]: "))
        row.append(val)
    C.append(row)

# Step 1: Multiply A and B → AB
AB=[]
for i in range(r1):
    row=[]
    for j in range(c2):
        sum=0
        for k in range(c1):
            sum+=A[i][k]*B[k][j]
        row.append(sum)
    AB.append(row)
ABC=[]
for i in range(r1):
    row=[]
    for j in range(c3):
        sum=0
        for k in range(c2):
            sum+=AB[i][k]*C[k][j]  
        row.append(sum)
    ABC.append(row)    
for row in ABC:
    print(row)                  

# Sum Of Diagonal Elememts

r=int(input("Enter rows:"))
c=int(input("Enter Columns:"))
if r!=c:
    print("Matrix Must Should be Sqaure Matrix:")
    exit

matrix=[]

for i in range(r):
    row=[]
    for j in range(c):
        values=int(input())
        row.append(value)
    matrix.append(row)

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()    

sum=0
for i in range(r):
    sum+=matrix[i][i]  
print("Sum od Diagonal Elements",sum)     


