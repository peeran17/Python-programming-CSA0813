# Problem 10 :Write a Python Program to Intersecting an elements
s1={1,2,3,45,5,6,3}
s2={1,2,3,9,6,5}
s=s1.intersection(s2)
print(s)


# problem 9 : Write a python program to store the arrays in non-increasing order
arr=[4,8,3,5,9]
arr.sort()
print(arr)


#8 Write a python program to find the average of mean median mode
arr=[24,54,67,98]
sum=0
count=len(arr)   
for i in arr:
    sum+=i
print(sum // count)


#problem 7 : Check whether the number is positive or negative
n=int(input("Enter A Number:"))

if n>0:
    print(n,'it is A Positive')
else:
    print("It is A Negative")

#problem 6 : Write a program to find out the duplicate array
arr=[1,2,3,3,4,4,5,6,6,]
unique_arr=[]
for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)
print(unique_arr)    



#problem 5 : Check whether Give Year is Leap Year or Not
year=int(input("Enter The Year:"))

if (year % 4 == 0 and year %100 !=0) or (year % 400 == 0):
    print(f'{year} is A Leap Year..')
else:
    print(f'{year} is Not a Leap Year ')  




#problem 4 : print the Multiplication Table
n=int(input("ENter The Multiplication N:"))
for i in range(1,10):
    print(n,'X',i,'=',n*i)




# 3.Suare Pattern
for i in range(1, 6):          
    for j in range(1, i+1):   
        print('*', end='')    
    print()                    
   
  
# problem 2  : Find The Sqaure And Cube Of Decimal Number
n=float(input("Enter The Float Values Only..."))
square=n**2
cube=n**3
print(square)
print(cube)

# Problem 1 : Read the number until -1 is encounter. find the avg of positive numbers and
negative numbers entered by user

print("Enter -1 to exit the loop")

pos_sum = 0
pos_count = 0
neg_sum = 0
neg_count = 0

while True:
    n = int(input("Enter the value: "))

    if n == -1:        
        break
    elif n > 0:         
        pos_sum += n
        pos_count += 1
    elif n < 0:         
        neg_sum += n
        neg_count += 1

if pos_count > 0:
    pos_avg = pos_sum // pos_count   
    print("avg positive number is", pos_avg)
else:
    print("No positive numbers entered")

if neg_count > 0:
    neg_avg = neg_sum // neg_count   
    print("avg negative number is", neg_avg)
else:
    print("No negative numbers entered")

