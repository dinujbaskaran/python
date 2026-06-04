for i in range(1,11):
    print ("2 X",i,"=",2*i)

for i in ("Apple"):
    print (i)

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
for i in range(a+1,b):
    print (i)

e_count = 0
o_count = 0
for i in range(1,11):
     if i%2==0:
        e_count = e_count + 1
     else:
        o_count = o_count + 1
print (o_count)
print (e_count)

count=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        count = count +1
print (count)

sum = 0
for i in range(1,6):
    sum = i + sum
print (sum)

sum=0
print("Enter the numbers :")
for i in range (1,11):
    num = int(input())
    sum = num + sum
    avg = sum /10
print ("Sum is",sum)
print ("Average is",avg)

a=[1,2,3,4,5]
# print (a[0])
# print (a[0:3])
for i in a:
    print ()

a=[]
a.append(10)
a.append(20)
a.append(30)
print(a)
    
a=[]
print("Enter 5 numbers")
for i in range (5):
    b=int(input("Enter the number "+str(i+1)+": "))
    a.append(b)
print(a)

a=[]
print("Enter 5 numbers")
for i in range (5):
    print ("Enter the number ",i+1,": ")
    b = int(input())
    a.append(b)
print(a)

sum = 0
for i in a:
    sum = sum + i
print ("Sum is :",sum)

a = []
b = int(input("Enter the range of numbers :"))
for i in range (1,b+1):
    a.append(i)
print(a)

b = int(input("Enter the range of numbers : "))
for i in range (1,b+1):
    print("Number is :",i,"and the cube of",i,"is :",i**3)
print ("Hello World, ", end ='???')
print("Dinuj")

# 

name = input("What's your name ? ")
age = input("How old are you ? ")
area = input("Where are you living ? ")
print(f"Hello, {name},You're {age} years old,You're living in {area}")

name = input("What's your name ? ")
name = name.strip()
print(f"Hello, {name}")

name = input("What's your name ? ")
name = name.upper()
print(f"Hello, {name}")

name = input("What's your name ? ")
name = name.capitalize()
print(f"Hello, {name}")

name = input("What's your name ? ")
name = name.title().strip()
print(f"Hello, {name}")

name = input("What's your name ? ").strip()
print(f"Hello, {name}")

name = input("What's your name ? ").capitalize()
first, last = name.split()
print(f"Hello, {first}")

x = float(input("Enter the number : "))
y = float(input("Enter the number : "))

z = x + y
print(f"Sum is {z:,}")


x = float(input("Enter the number : "))
y = float(input("Enter the number : "))

z = round(x / y, 2)
print(z)
print(f"{z:.2f}")

def hello():
    print("Hello World")

name = input("What's your name ?").strip().capitalize()
hello()
print(name)
