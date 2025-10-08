Reverse an array without using built-in functions
arr = [1, 2, 3, 4, 5]
rev = []
for i in range(len(arr)-1, -1, -1):
    rev.append(arr[i])
print("Reversed Array:", rev)


Output:
Reversed Array: [5, 4, 3, 2, 1]

🟩 2️⃣ Find the maximum and minimum element
arr = [10, 25, 5, 30, 15]
max_ele = arr[0]
min_ele = arr[0]
for i in arr:
    if i > max_ele:
        max_ele = i
    if i < min_ele:
        min_ele = i
print("Max:", max_ele)
print("Min:", min_ele)


Output:
Max: 30
Min: 5

🟩 3️⃣ Sum and average of array elements
arr = [10, 20, 30, 40]
total = 0
for i in arr:
    total += i
avg = total / len(arr)
print("Sum:", total)
print("Average:", avg)


Output:
Sum: 100
Average: 25.0

#️⃣ Frequency of each element
arr = [1, 2, 2, 3, 1, 4, 2]
freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Frequency:", freq)


Output:
Frequency: {1: 2, 2: 3, 3: 1, 4: 1}

#️⃣ Linear search
arr = [5, 10, 15, 20, 25]
key = 15
found = False
for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break
if not found:
    print("Element not found")


Output:
Element found at index 2

#️⃣ Sort in ascending & descending order (without built-ins)
arr = [3, 1, 4, 2]
# Ascending
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print("Ascending:", arr)

# Descending
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print("Descending:", arr)


Output:
Ascending: [1, 2, 3, 4]
Descending: [4, 3, 2, 1]

#️⃣ Merge two arrays
a = [1, 2, 3]
b = [4, 5, 6]
merged = []
for i in a:
    merged.append(i)
for i in b:
    merged.append(i)
print("Merged Array:", merged)


Output:
Merged Array: [1, 2, 3, 4, 5, 6]

#️⃣ Find index of an element
arr = [10, 20, 30, 40]
x = 30
for i in range(len(arr)):
    if arr[i] == x:
        print("Index of", x, "is", i)
        break


Output:
Index of 30 is 2

#️⃣ Remove duplicates
arr = [1, 2, 2, 3, 3, 4]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print("After removing duplicates:", unique)


Output:
After removing duplicates: [1, 2, 3, 4]

# Rotate array by k (left)
arr = [1, 2, 3, 4, 5]
k = 2
rotated = arr[k:] + arr[:k]
print("Left rotated by", k, ":", rotated)


Output:
Left rotated by 2 : [3, 4, 5, 1, 2]

# Second largest & second smallest
arr = [10, 40, 20, 30]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print("Second Smallest:", arr[1])
print("Second Largest:", arr[-2])


Output:
Second Smallest: 20
Second Largest: 30

# Copy all elements to another array
arr = [1, 2, 3, 4]
copy = []
for i in arr:
    copy.append(i)
print("Copied Array:", copy)


Output:
Copied Array: [1, 2, 3, 4]

# Difference between largest & smallest
arr = [10, 5, 20, 8]
maxi = arr[0]
mini = arr[0]
for i in arr:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
print("Difference:", maxi - mini)


Output:
Difference: 15

# Split array into two halves
arr = [1, 2, 3, 4, 5, 6]
mid = len(arr)//2
first = arr[:mid]
second = arr[mid:]
print("First Half:", first)
print("Second Half:", second)


Output:
First Half: [1, 2, 3]
Second Half: [4, 5, 6]

# Insert an element at a specific index
arr = [1, 2, 4, 5]
index = 2
value = 3
arr = arr[:index] + [value] + arr[index:]
print("After insertion:", arr)


Output:
After insertion: [1, 2, 3, 4, 5]

# Delete an element from an array
arr = [10, 20, 30, 40]
val = 30
new = []
for i in arr:
    if i != val:
        new.append(i)
print("After deletion:", new)


Output:
After deletion: [10, 20, 40]

#19 Replace all negative numbers with zero
arr = [2, -3, 4, -5, 6]
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0
print("After replacing:", arr)


Output:
After replacing: [2, 0, 4, 0, 6]
# 20 Print all pairs whose sum = given number
arr = [1, 2, 3, 4, 5, 6]
target = 7
print("Pairs with sum", target, ":")
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], "+", arr[j])
