# Functions : Mainly these Are Used to Perform a specific task ,multiple times without writing the same code again and again
# Simply : functions Are used to be Code Reusability
# These are User Defined Function And These Are 4
#1 .without arg,without return value : just Simply to perform 
# Syntax : def functionname():
#                 function of the body
#           functioncalling()  , def - Keyword to define as function
# Problems in Type 1  : Without arg,without return 
def name():
    print("Hallo Whats Ur Name ,why are U texting me,what the fuck your doing")
name()  
name()  
print("Hii")
#Write a function to display the first 10 natural numbers.
def num():
    n=int(input("Enter How many Natural Numbers need :"))
    for i in range(1,n+1):
        print(i)
num() 
num() 

# Print Even Numbers Upto 30
def even():
    n=int(input("Enter How Many EVen Numbers Do u nee to Display:"))
    for i in range(1,n+1):
        if i % 2 == 0:
            print("Even Numbers :",i)
even()  

#2️⃣ Function with Arguments and without Return Value

#➡️ Takes input values but only prints results (no return).
# Ex :
def add(a, b):
    print("Sum is:", a + b)
    
add(5, 3)

# 1.Write a function that accepts two numbers and prints their sum.
def sum(a,b):
    c=a+b
    print(f"sum ={c}")
sum(12,0) 

#Write a function that takes a name and prints a greeting message.
def greet(name):
    print(f"{name},Wish U a Very Happy Birthday!..")
    print("a Great Head Dear...")
greet("peeran")  

#Prints The Grade Based on the Markss
def grade(n):
    if n>90:
        print(f"Grade = A")
    elif n>80:
        print("grade = B")
    else:
        print("Fail") 
grade(88)
grade(99)               
#Write a function that accepts a number and prints its multiplication table.
def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
table(78)
table(19)
table(16)

##  Type 3 : Without arguments but with return Value
# Ex:
def greet():
    return "Hey Peer Happy Birthday"


gr=greet()
print(gr)

#To find The Factorial using retrn
def factorial():
    n=int(input("Enter N Value FOr Factorial"))
    fact=1
    for i in range(1,n+1):
        fact*=i

    return fact

result=factorial()
print("Factorila of",'=',result)  

# Print the Smalest Element in the List
def small():
    list1=[4,6,1,7,3]
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i] > list1[j]:
                list1[i],list1[j]=list1[j],list1[i]
        return list1[0] 
smallest=small()
print("Smallest Element",smallest)  



#Type 4 : 4️⃣ Function with Arguments and with Return Value

#➡️ Takes input and returns output.

# 1.Write a function that takes a string and returns the number of vowels.
def vowel(s):
    v='aeiouAEIOU'
    count=0
    for ch in s :
        if ch in v:
            count+=1
    return count        

vowels=vowel("peeran")
print(f"No.of Vowels ={vowels}")

#Write a function that takes a list and returns the largest element.
def largest(l):
    print("List entered:", l)
    l.sort(reverse=True)
    return l[0]

list1 = list(map(int, input("Enter values: ").split()))
largest_num = largest(list1)
print("Largest number is:", largest_num)

#Write a function that takes a number and returns True if it’s prime, else False.
def is_prime(n):
    if n>1:
        prime=True
        for i in range(2,n):
            if n% i == 0:
                return "Not prime"
            return "prime"
        else:
            return " prime"
t=int(input("Enter Number To Check prime or Not"))
prime_number=is_prime(t)   
print(prime_number)


#Now We are Going to Solve Top 10 Problems :
def square(n):
    sqq=(n**2)
    return sqq
def cube(n):
    cub=(n**3)
    return cub

t=int(input("Enter Number TO find Squaare And Cube: "))
sq=square(t) 
cb=cube(t) 
print("Suare =",sq)  
print("Cube = ",cb)

# Write a function that checks whether a string is palindrome or not.
def palindrome(name):
    s=name[::-1]
    if name == s:
        return "Palindrome"
    return"Not palindrome"
str=palindrome('madam')
print(str)    
# Write a Python Code for To check Armstrong Number
def armstrong_num(n):
    q=0
    temp=n
    while n>0:
        p=n%10
        q=(p**3)+q
        n=n//10
    if temp == q:
        return "Armstrong Number"
    else:

        return "Not Armstrong Number"
y=int(input("Enter Number:")) 
result=armstrong_num(y)  
print(result)     

#2️⃣ Function with Arguments and without Return Value

#➡️ Takes input values but only prints results (no return).
# Ex :
def add(a, b):
    print("Sum is:", a + b)
    
add(5, 3)

# 1.Write a function that accepts two numbers and prints their sum.
def sum(a,b):
    c=a+b
    print(f"sum ={c}")
sum(12,0)    




