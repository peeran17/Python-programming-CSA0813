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



