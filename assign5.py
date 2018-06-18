#question1

year= int(input("enter a year :"))
if (year%400==0):
    print("%d is a leap year"%year)
else:
    print("%d is not a leap year"%year)

#question2

length= input("enter the length")
breadth= input("enter the breadth")
if(length==breadth):
    print("sqaure")
else:
    print("rectangle")

#question3

a= input("enter the age")
b= input("enter the age")
c= input("enter the age")
if(a>b):
    if(a>c):
        print("a is greater")
elif((b>c) & (b>a)):
    print("b is greater")
else:
    print("c is greater")

#questiom4

a= int(input("number scored"))
if (a>=1 and a<=50):
    print("no price")
elif (a>=51 and a<=150):
    print(" congratulations you won wooden")
elif (a>=151 and a<=180):
    print(" won book")
elif (a>=181 and a<=200):
    print("won chocolate")
else :
    print("sorry no price")

#question5

a= int (input("enter the quantity of items"))
b= a*100
if (b>1000):
    c=b*0.1
    d=b-c
    print("discount given is")
    print(c)
    print("cost after discount is")
    print(d)
else:
    print("sorry no discount")







