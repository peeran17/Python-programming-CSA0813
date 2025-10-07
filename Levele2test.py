# Matrix 
r = int(input("Enter Number Of Rows: "))
c = int(input("Enter Number Of Columns: "))
matrix = []

# Taking input for matrix:
for i in range(r):
   row=[]
   for j in range(c):
        value=int(input(f"Enter the Number of Values [{i}][{j}]"))
        row.append(value)
   matrix.append(row)    

for i in range(r):
    for j in range(c):
     print(matrix[i][j],end=" ")
    print() 
 
       

# Taking input for matrix
for i in range(r):
    row = []
    for j in range(c):
        value = int(input(f"Enter The Values[{i}][{j}]: "))
        row.append(value)
    matrix.append(row)   # must be inside outer loop

# Printing the matrix
print("\nThe Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()   # new line after each row
 
   
       
       

      
       
     
  
    





#1 To count all the prime numbers and composite numbers
#Sample input: 4,54,29,71,59,98,23
#Output: composite numbers=3
#
# Prime numbers = 5

arr=list(map(int,input("Enter Numbers").split()))
prime_count=0
composite_count=0
for num in arr:
    if num>1:
        is_prime=True
        for i  in range(2,int(num**0.5)+1):
           if num % i == 0:
             is_prime=False
             break
    if is_prime:
     prime_count+=1
    else:
     composite_count+=1
print(f"Prime Count={prime_count}") 
print(f"Composit count={composite_count}")



#9 You are give with an array which contains integer element. Sort the elements. in non-increasing order and print the middle element of the array.
arr=list(map(int,input("Enter The Values:").split()))
arr.sort(reverse=True)




# 8Write a Python program to find largest 2nd maximum in array

arr=list(map(int,input(" ENter The Values :").split()))
arr.sort(reverse=True)
print(arr[1]," is the Second Largest Array")

#7 Write a Python program to display customer name mobile number and cost of the purchase.calculate the discount and find the total amount to be paid.
Customer_name=input("Enter Customer Name:")
mobile_number=int(input("Enter Your Mobile Nmber:"))
purchase_amount=int(input("Enter Your Purchase Amount"))
discount= (purchase_amount) *(15/100)
total_amount = discount+purchase_amount


print(f"Customer Name:{Customer_name}")
print(f"Mobile Number:{mobile_number}")
print(f"total Amount To Be Paid:{total_amount}")

# 6 Find GCD and LCM in Python
x=int(input("Enter The Value 'A"))
y=int(input("Enter Value 'B"))
a, b =x, y
while b!=0:
    a, b=b,a%b
gcd=a
lcm=(x * y) // gcd
print(gcd)
print(lcm)

# 5  Find the Mth maximum number and Nth minimum number in an array and find the sum and difference of it.
arr=list(map(int,input(" ENter The Values :").split()))
arr.sort(reverse=True)
l=len(arr)
a=arr[0]
b=arr[l-1]
print(f"{a} is The First Largest Value in The Array")
print(f"{b} is the Second Largest Number In Array")
print(a+b," is the Sum of Two Values")
print(a-b," is the Difference Of Two Values")



#  Write a program in Python to read the elements of a one-dimensional array,
#compare the elements and find which are the largest two elements in a given
#array.

arr=list(reverse=True)
print(arr)(map(int,input("Enter Values").split()))
arr.sor
print(arr[0],"is the first Largest Number")
print(arr[1]," is the Second Largest Number")

#3.3 Perfect number or not  Hint : Sum of Divisors of N =N Value is Called  perfect Number
n=int(input("Enter a Number To check Perfect:"))
sum_divisors=0
for i in range(1,n):
    if n % i == 0:
        sum_divisors+=i
if sum_divisors == n:
    print(n," Is a Perfect Number ..")   
else :
    print(" it is not A Perfect")         


# Write a program in Python to read the elements of a one-dimensional array,
#compare the elements and find which are the largest two elements in a given
#array.

arr=list(map(int,input("Enter Values").split()))
