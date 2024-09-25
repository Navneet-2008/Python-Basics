#taking input from the user and printing it
name=input("name: ")
age= int(input ("age: "))
price= float(input ("price: "))
print("my name is", name , "and my age is", age)

light = input("light colour is : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken ")
