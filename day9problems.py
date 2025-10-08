# Lets Solve 10 Problems on Todays Session 
#List,tuple,string,set,Dictionary

# Dictionary Problems 

#✅ With these 10 problems, you cover:

#Creating, accessing, updating, deleting

#Looping through dicts

#Frequency count (common interview)

#Merging dicts

#Dictionary comprehension

#max/min usage

#zip() usag

# 1 .Create a new Dicyionary and Access the Elements 
dict1={"Name":"Peeran BAshas ","age":18,"Mother":"peerambi","Father":"Peeru","Bro":"khasim","Area":"Rajupeta"}
print(dict1,type(dict1))

# Add New Key value
dict1["Study"]="Chennai"
print(dict1)

# update
dict1["age"]=19
print(dict1)

#Remove
del dict1["age"] 
print(dict1)

#Loop Throgh Key values and PAirs
dict1={"Name":"Peeran BAshas ","age":18,"Mother":"peerambi","Father":"Peeru","Bro":"khasim","Area":"Rajupeta"}
for key,value in dict1.items():
    print(key, ":",value)

#Count frequency of characters in a string (common interview question)    

text='banana'
freq={}
for char in text:
    freq[char]=freq.get(char,0)+1
print(freq)    


#Merge Two Dictionaries :    Use d1.update(d2)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)


marks = {"math": 90, "science": 95, "english": 88}

subject = max(marks, key=marks.get)
print("Highest marks in:", subject)   # science


# Convert Two List into Dictionaries
keys=["name","milk","gender"]
values=["bahset","normal","telidu"]
dict3=dict(zip(keys,values))
print(dict3)



# We Are Going To Solve Problems On  Sets
#Unique Numbers
list1=[1,2,3,4,5,6,7]
sets=set(list1)
print(sets)

# Write a program to take two sets of integers from the user and print their
set1 = {int(x) for x in input("Enter elements for Set1 (space separated): ").split()}
set2 = {int(x) for x in input("Enter elements for Set2 (space separated): ").split()}
print(set1)
print(set2)  

setr=set1.union(set2)
print(setr)

setr=set1.intersection(set2)
print(setr)

setr=set1.difference(set2)
print(setr)

setr=set1.symmetric_difference(set2)
print(setr)

#
# Menu-driven program for Set Operations

# Taking input as set
set1 = {int(x) for x in input("Enter elements for Set1 (space separated): ").split()}
set2 = {int(x) for x in input("Enter elements for Set2 (space separated): ").split()}

while True:
    print("\n--- Set Operations Menu ---")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference (Set1 - Set2)")
    print("4. Difference (Set2 - Set1)")
    print("5. Symmetric Difference")
    print("6. Subset Check (Set1 ⊆ Set2)")
    print("7. Superset Check (Set1 ⊇ Set2)")
    print("8. Disjoint Check")
    print("9. Exit")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        print("Union:", set1 | set2)

    elif choice == 2:
        print("Intersection:", set1 & set2)

    elif choice == 3:
        print("Difference (Set1 - Set2):", set1 - set2)

    elif choice == 4:
        print("Difference (Set2 - Set1):", set2 - set1)

    elif choice == 5:
        print("Symmetric Difference:", set1 ^ set2)

    elif choice == 6:
        print("Set1 is subset of Set2:", set1.issubset(set2))

    elif choice == 7:
        print("Set1 is superset of Set2:", set1.issuperset(set2))

    elif choice == 8:
        print("Set1 and Set2 are disjoint:", set1.isdisjoint(set2))

    elif choice == 9:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter between 1-9.")

# Student Subjects
A={x for x in input("Enter Players Who play Only Cricket:").split()}
B={x for x in input("Enter Players Who play Only Football:").split()}

## 1. Students who play bot
both= A&B
print("Stduents Play Both :",both)

## 2. Students who play only Cricket
only_cricket=A-B
print("Stduents play only cricket:",only_cricket)

#3.Sytudents who play Volleyball
volleyball=B-A
print("Students Play only Volleyball:",volleyball)

#4.Students who Play Either Cricket or Volleyball
either=A ^ B
print("Students will Play Either Cricket or Volleyball:",either)


# Lets See Problems on Strings 

# Reverse A String
peru="jasmin"
print(peru[::-1])

# Palindrome hint : fron to last and last to front whatevr it should be same string
S=input("enter a string")
Z=S[::-1]
if S == Z:
    print(f"{S} is a Palindrome")
else:
    print("Not ")   


# Count ,consonants Vowels in A String
N=input("Enter A String :")
count=0
con=0
for char in N:
    if char in 'aeiouAEIOU':
        count=count+1
    elif char not in 'aeioeAEIOU':
        con=con+1    
print(f'Vowels :{count}')    
print(f'Consonants:{con}')    


#. Count frequency of each character
s='ananaunana'
freq={}
for char in s:
    freq[char]=freq.get(char,0)+1
print(freq)