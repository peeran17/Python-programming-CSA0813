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
