# All function
#Function 1  ----- Calculator
def calculator (a,b,c):
    if b == '+' :
        print("The value of",a ,"+",c ,"is",a+c)
    if b == '-':
         print ("The value of",a ,"-",c ,"is",a-c)
    if b == '*':
        print("The value of",a ,"*",c ,"is",a*c)
    if b == '/' :
        print("The value of",a ,"/",c ,"is",a/c)


#Function 2 ----- Factor
def factor(n):
    i = 0
    if  0<n:
        print ( "Factor of ",n,"is ")
    elif 0>n :
        print("Error in your number \n please check \n 1.your number is positve or not \n 2. Your number is integer or not" )
    while n>i:
        i = i+1
        if n%i == 0: 
            print (i)


#Function 3 ----- Number
def number (a):
    if a%2 == 0:
        print("Even number \n Natural number \n Whole number")
    if a%2 != 0:
         print("Odd number  \n Natural number \n Whole number")
    if a == 0 :
         print(" whole number")
    if a == 1:
        print ("Not primes")
    elif a%4 != 0 and a%6 != 0:
         print("Prime number ")
    else:
        print("not prime")


#Fuction 4 ----- Table
def table(a):
    for f in range(11):
         print(a,"*",f,"=",f*a)


#Function 5 ----- Square
def square (a):
    print("Square  of",a , "is", a*a)


#Function 6 ----- Cube
def cube (a):
    print("cube  of",a , "is", a*a*a)
    

#Function 7 ----- Age
def age (b , c):
    print("your age is",c-b,"/",b)


 #Main  

print("Hello, What you find \n (a) calculator\n (b) factor \n (c) number \n (d) table \n (e) square \n (f) cube \n (g) age")
print("Choose number of 1 to 7 ")
find = str(input())
print("Ok you choosse is    ",find,  )

if find == "a":
    print("Solve problems")
    a = int(input())
    b = input()
    c = int(input())
    calculator(a,b,c)
    
elif find == "b":
    print("find factor of any number")
    n = int(input())
    factor(n)

elif find =="c":
    print("Enter a number")
    a = int(input())
    number(a)

elif find == "d":
    print("Write a number for table")
    a = int(input())
    table(a)
    
elif find == "e":
    print("Enter a number")
    a = int(input())
    square(a)

elif find == "f":
    print("Enter a number")
    a = int(input())
    cube(a)

elif find == "g":
    print("Write your born year ")
    a = int(input())
    print("Which year it is")
    b = int(input())
    print("Your Data is ===>")
    age(a,b) 

else :
    print("Error in your choice")
    
print('Do you want to play again? (Y/N)')
ans = input().lower()
if ans == 'n':
    print('Thanks for playing!')

