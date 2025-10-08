# Print star pattern
# 4 steps for Any Pattern printing :
#1 : Outerloop - it Counts Number of Lines(rows)
#2 : innerloop - it for columns  and (connect * to the rows)
#3: always print the "*" inside And inner loop
# Symmetric

# 1.Right-angled Triangle
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()  
# 2.inverted R.triangle
n=int(input("Enter Number of Rows:"))
for i in range(0,n):
    for j in range(0,n-i):
        print("*",end="")
    print()    

#3.Pyramid
n=int(input("Enter Number of Rows"))

for i in range(1,n+1):
    for space in range(1,n-i+1):                   # Void spaces before printing the stars =rows-rownumber
        print(" ",end='')
    for j in range(1,i+1):
        print('*',end=" ")

    print()        

# daimond 
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

# Hallow Sphere
n=int(input("Enter number of rows:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(' ',end="")
    print()            

#Pascals Triangle
n=int(input("Enter Number Of Rows:")) 
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=" ")
    num=1
    for j in range(1,i+1):
        print(num,end="")
        num=num*(i-j) // j
    print()        
