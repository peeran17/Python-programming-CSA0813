

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Step 1: Find GCD
a, b = x, y
while b != 0:
    a, b = b, a % b
gcd = a

# Step 2: Apply formula for LCM
lcm = (x * y) // gcd

print("GCD is:", gcd)
print("LCM is:", lcm)
