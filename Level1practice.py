# Here There Are The Codes for it helps to Undnerastand the Level 1 Concept
# 1.Area Of rectangle
l=int(input("Enter the Lenght:"))
b=int(input("Enter the breadth:"))
a=l*b
print("Area Of the Rectangle is ",a)

#2.Greatest of Three numbers 
a=int(input("enter The Number:"))
b=int(input("enter The Number:"))
c=int(input("enter The Number:"))
if a>b and a>c:
    print(a,'is the Greatest.')
elif b>c:
    print(b,'Is the greatest.')    
else:
    print(c,'is the greatest')    

#
# 1. Area of Rectangle
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
print("Area of Rectangle =", l*b)

#2. Area of Circle
r = float(input("Enter radius: "))
print("Area of Circle =", 3.14*r*r)

#3. Area of Cuboid
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))
print("Area of Cuboid =", 2*(l*b + b*h + l*h))

#4. Area of Cube
a = float(input("Enter side: "))
print("Area of Cube =", 6*a*a)

#5. CSA of Cylinder
r = float(input("Enter radius: "))
h = float(input("Enter height: "))
print("CSA of Cylinder =", 2*3.14*r*h)

#6. TSA of Cylinder
r = float(input("Enter radius: "))
h = float(input("Enter height: "))
print("TSA of Cylinder =", 2*3.14*r*(r+h))

#7. CSA of Cone
r = float(input("Enter radius: "))
l = float(input("Enter slant height: "))
print("CSA of Cone =", 3.14*r*l)

#8. TSA of Right Circular Cone
r = float(input("Enter radius: "))
l = float(input("Enter slant height: "))
print("TSA of Cone =", 3.14*r*(r+l))

#9. TSA of Sphere
r = float(input("Enter radius: "))
print("TSA of Sphere =", 4*3.14*r*r)

#10. Volume of Cuboid
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))
print("Volume of Cuboid =", l*b*h)

#11. Volume of Cube
a = float(input("Enter side: "))
print("Volume of Cube =", a**3)

#12. Volume of Cylinder
r = float(input("Enter radius: "))
h = float(input("Enter height: "))
print("Volume of Cylinder =", 3.14*r*r*h)

#13. Volume of Cone
r = float(input("Enter radius: "))
h = float(input("Enter height: "))
print("Volume of Cone =", (1/3)*3.14*r*r*h)

#14. Volume of Sphere
r = float(input("Enter radius: "))
print("Volume of Sphere =", (4/3)*3.14*r**3)

#15. Perimeter of Rectangle
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
print("Perimeter of Rectangle =", 2*(l+b))

#16. Area of Square
a = float(input("Enter side: "))
print("Area of Square =", a*a)

#17. Area of Triangle
b = float(input("Enter base: "))
h = float(input("Enter height: "))

print("Area of Triangle =", 0.5*b*h)    

18# Gratest Of  4 numbers 
a,b,c,d = map(int,input("Enter 4 numbers: ").split())
print("Greatest =", max(a,b,c,d))

20# MarkList Division
m=int(input("Enter your Marks :"))
if(m>=90):
    print('A')
elif m>=80:
    print('B')
elif m>=60:
    print('C')
else:
    print("FAIL !")    

21. Program to find factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "is", fact)

22. Program to check whether a number is palindrome
n = int(input("Enter number: "))
temp = n
rev = 0
while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n //= 10
if temp == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

23. Program to check whether a number is prime or not
n = int(input("Enter number: "))
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")

24. Program to print Fibonacci series
n = int(input("Enter number of terms: "))
a, b = 0, 1
print(a, b, end=" ")
for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a, b = b, c

25. Program to find the sum of digits of a number
n = int(input("Enter number: "))
sum = 0
while n > 0:
    d = n % 10
    sum += d
    n //= 10
print("Sum of digits:", sum)

26. Program to check Armstrong number
n = int(input("Enter number: "))
temp = n
sum = 0
while n > 0:
    d = n % 10
    sum += d ** 3
    n //= 10
if temp == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

27. Program to find reverse of a number
n = int(input("Enter number: "))
rev = 0
while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n //= 10
print("Reverse of number:", rev)

28. Program to find the largest of three numbers
a, b, c = map(int, input("Enter three numbers: ").split())
if a > b and a > c:
    print(a, "is largest")
elif b > c:
    print(b, "is largest")
else:
    print(c, "is largest")

29. Program to find the smallest of three numbers
a, b, c = map(int, input("Enter three numbers: ").split())
if a < b and a < c:
    print(a, "is smallest")
elif b < c:
    print(b, "is smallest")
else:
    print(c, "is smallest")

30. Program to check even or odd
n = int(input("Enter number: "))
if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

31. Program to find LCM of two numbers
a, b = map(int, input("Enter two numbers: ").split())
maxi = max(a, b)
while True:
    if maxi % a == 0 and maxi % b == 0:
        print("LCM is", maxi)
        break
    maxi += 1

32. Program to find GCD of two numbers
a, b = map(int, input("Enter two numbers: ").split())
while b != 0:
    a, b = b, a % b
print("GCD is", a)

33. Program to swap two numbers
a, b = map(int, input("Enter two numbers: ").split())
a, b = b, a
print("After swapping:", a, b)

34. Program to find area of circle
r = float(input("Enter radius: "))
area = 3.14159 * r * r
print("Area of circle:", area)

35. Program to find area of rectangle
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
area = l * b
print("Area of rectangle:", area)

