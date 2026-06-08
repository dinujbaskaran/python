# for i in range(1,11):
#     print ("2 X",i,"=",2*i)

# for i in ("Apple"):
#     print (i)

# a = int(input("Enter the number a: "))
# b = int(input("Enter the number b: "))
# for i in range(a+1,b):
#     print (i)

# e_count = 0
# o_count = 0
# for i in range(1,11):
#      if i%2==0:
#         e_count = e_count + 1
#      else:
#         o_count = o_count + 1
# print (o_count)
# print (e_count)

# count=0
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         count = count +1
# print (count)

# sum = 0
# for i in range(1,6):
#     sum = i + sum
# print (sum)

# sum=0
# print("Enter the numbers :")
# for i in range (1,11):
#     num = int(input())
#     sum = num + sum
#     avg = sum /10
# print ("Sum is",sum)
# print ("Average is",avg)

# a=[1,2,3,4,5]
# # print (a[0])
# # print (a[0:3])
# for i in a:
#     print ()

# a=[]
# a.append(10)
# a.append(20)
# a.append(30)
# print(a)
    
# a=[]
# print("Enter 5 numbers")
# for i in range (5):
#     b=int(input("Enter the number "+str(i+1)+": "))
#     a.append(b)
# print(a)

# a=[]
# print("Enter 5 numbers")
# for i in range (5):
#     print ("Enter the number ",i+1,": ")
#     b = int(input())
#     a.append(b)
# print(a)

# sum = 0
# for i in a:
#     sum = sum + i
# print ("Sum is :",sum)

# a = []
# b = int(input("Enter the range of numbers :"))
# for i in range (1,b+1):
#     a.append(i)
# print(a)

# b = int(input("Enter the range of numbers : "))
# for i in range (1,b+1):
#     print("Number is :",i,"and the cube of",i,"is :",i**3)
# print ("Hello World, ", end ='???')
# print("Dinuj")

# # 

# name = input("What's your name ? ")
# age = input("How old are you ? ")
# area = input("Where are you living ? ")
# print(f"Hello, {name},You're {age} years old,You're living in {area}")

# name = input("What's your name ? ")
# name = name.strip()
# print(f"Hello, {name}")

# name = input("What's your name ? ")
# name = name.upper()
# print(f"Hello, {name}")

# name = input("What's your name ? ")
# name = name.capitalize()
# print(f"Hello, {name}")

# name = input("What's your name ? ")
# name = name.title().strip()
# print(f"Hello, {name}")

# name = input("What's your name ? ").strip()
# print(f"Hello, {name}")

# name = input("What's your name ? ").capitalize()
# first, last = name.split()
# print(f"Hello, {first}")

# x = float(input("Enter the number : "))
# y = float(input("Enter the number : "))

# z = x + y
# print(f"Sum is {z:,}")


# x = float(input("Enter the number : "))
# y = float(input("Enter the number : "))

# z = round(x / y, 2)
# print(z)
# print(f"{z:.2f}")

# def hello(to):
#     print(f"Hello, {to}!")

# name = input("What's your name ?").strip().capitalize()
# hello(name)

# def hello(to):
#     print("Hello,",to)

# name = input("What's your name? ").capitalize()
# hello(name)

# def add(x,y):
#     z = x + y
#     print(z)

# def sub(x,y):
#     z = x - y
#     print (z)

# def div(x,y): 
#     z = x / y
#     print(f"{z:.2f}")    


# num1= int(input("What's the value of x : "))
# num2 = int(input("What's the value of y : "))
# add(num1,num2)
# sub(num1,num2)
# div(num1,num2)

# def findevenorodd(x):
#     if x >=0:
#         if x % 2 ==0:
#             print("even")
#         else:
#             print("odd")
#     else:
#         print("Invalid No.")

# x = int(input("What's the value of x : "))
# findevenorodd(x)

# def findpassorfail(score):
#     if score > 35 :
#         print("Pass")
#     else:
#         print("fail")

# a = int(input("Enter the marks : "))
# findpassorfail(a)

# def rangea(x,y):
#     if y > x :
#         for i in range(x,y+1):
#             print(x," ",end="")
#             x = x + 1
#     else:
#         print("Invalid range")    

# p = int(input("Enter the number from the range starts : "))
# q = int(input("Enter the number which the range start end : "))
# rangea(p,q)

# def hello():
#     print("Hello, ", name)

# name = input("What's your name? :").capitalize()
# hello()

# def main():
#     name = input("What's your name? :").capitalize()
#     hello(name)

# def hello(name):
#     print(f"Hello ,{name}")

# main()

# a=10
# a=a**a
# print(a)

# def main():
#     x = int(input("What's the value of x? :"))
#     print("x square is",square(x))

# def square(n):
#     return n**2
# main()

# a=3 
# print(type(a))

# def get():
#     guess = int(input("Enter a guess :"))
#     return guess

# def main():
#     guess = get()
#     print(guess)
#     print(type(guess))

main()

vanakam = "Good morning, "

def main():
    global vanakam
    hello("Is anyone there? ")
    vanakam = "Good evening, "
    hello("Ohhh,Hi ")

def hello(input):
    name = "Invalid"
    print(input,vanakam)

name = input("What's your name? ")

main()

name = input("What's your name? ")
print("Good morning, ",name)

marks = int(input("What's your marks: "))
if marks >= 75:
    print("A")
elif marks >= 65:
    print("B")
elif marks >= 55:
    print("C")
elif marks >= 45:
    print("S")
else:
    print("F")

def main():
    x = int(input("What's your x? :"))
    if even_odd(x):
        print("Even")
    else:
        print("Odd")

def even_odd(n):
    if n % 2 == 0:
        return True
    else:
        return False

def even_odd(n):
    return True if n % 2 == 0 else False

def even_odd(n):
    return n % 2 == 0

main()

name = input("What's your name ? ").capitalize()

match name:
    case "Dinuj" |"Sarvathan":
        print("Kondavil")        
    case "Piraveen":
        print("Kokuvil")    
    case "Bachu":
        print("Jaffna Town")    
    case "Vindu":
        print("Vadukottai")    

