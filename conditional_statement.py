age=14
if(age>=18):
    print("vote")
else:
    print("cannot vote")

#practice questions
marks=78
if(marks>= 90):
    print("grade=A")
elif(marks>=80 and marks<90):
    print("grade=B")
elif(marks>=70 and marks<80):
    print("grade=C")
elif(marks<70):
    print("grade=D")
else:
    print("grade=F")

#practice questions
num=2
if(num%2==0):
    print("even")
else:
    print("odd")

a= int(input("the value of a : "))
b= int(input("the value of b : "))
c= int(input("the value of c : "))

# if(a>b and a>c ):
#     print("a is the greatest number")
# elif(b>a and b>c):
#     print("b is the greatest number")
# else:
#     print("c is the greatest number")

if(a > b):
    if(a > c):
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if(b > c):
        print("b is greatest")
    else:
        print("c is greatest")

num=49
if(num%7==0):
    print("it is a multiple of 7")
else:
    print("it is not a multiple of 7")
