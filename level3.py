#1️⃣ Most and Least Significant Digit
n=int(input("Enter number:"))
s=str(n)
print("LSB:",s[0],"& MSB:",s[-1])


#Input: 1267899
#Output: LSB: 1 & MSB: 9

#2️⃣ Sum of squares (1² + 2² + ... + N²)
n=int(input("Enter n:"))
s=0
for i in range(1,n+1):
    s+=i*i
print(s)


#Input: 4
#Output: 30

#3️⃣ Tech Number Check
n=int(input("Enter number:"))
s=str(n)
l=len(s)
if l%2==0:
    a=int(s[:l//2])
    b=int(s[l//2:])
    print(n==((a+b)**2))
else:
    print(False)


#Input: 2025
#Output: True

#4️⃣ Decimal to Binary
n=int(input("Enter decimal:"))
b=""
while n>0:
    b=str(n%2)+b
    n//=2
print(b)


#Input: 7
#Output: 111

#5️⃣ All Combinations of Three Digits
nums=[1,2,3]
for i in nums:
    for j in nums:
        for k in nums:
            if i!=j and j!=k and i!=k:
                print(i,j,k)




#6️⃣ Max Profit with 2 Transactions
prices=[7,1,5,3,6,4]
buy1=buy2=float('inf')
profit1=profit2=0
for p in prices:
    buy1=min(buy1,p)
    profit1=max(profit1,p-buy1)
    buy2=min(buy2,p-profit1)
    profit2=max(profit2,p-buy2)
print(profit2)


#Output: 7

#7️⃣ Rotated Array
nums=[0,1,4,4,5,6,7]
k=int(input("Enter rotation times:"))
rotated=nums[-k:]+nums[:-k]
print(rotated)


#Input: 4
#Output: [4, 5, 6, 7, 0, 1, 4]

#8️⃣ Find Starting and Ending Index of Target
nums=[5,7,7,8,8,10]
target=int(input("Enter target:"))
start=-1
end=-1
for i in range(len(nums)):
    if nums[i]==target:
        if start==-1:
            start=i
        end=i
print([start,end])


#Input: 8
#Output: [3,4]

#9️⃣ Remove K Digits to Make Smallest Number
num=input("Enter number: ")
k=int(input("Enter k: "))
stack=[]
for d in num:
    while k>0 and stack and stack[-1]>d:
        stack.pop()
        k-=1
    stack.append(d)
res=''.join(stack[:-k] if k else stack).lstrip('0')
print(res if res else "0")


#Input: 1432219, 3
#Output: 1219

#🔟 Print Matrix in Spiral Order
matrix=[[1,2,3],[4,5,6],[7,8,9]]
res=[]
while matrix:
    res+=matrix[0]
    matrix=matrix[1:]
    if not matrix:break
    matrix=list(zip(*matrix))[::-1]
print(list(res))


#Output:
[1, 2, 3, 6, 9, 8, 7, 4, 5]
