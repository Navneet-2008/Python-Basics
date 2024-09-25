# take input of 3 numbers a, b and c
# then print the smallest number among them

a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))

if(a<b and a<c):
    print("a is the smallest number")
elif(b<a and b<c):
    print("b is the smallest number")
else:
    print("c is the smallest number")

