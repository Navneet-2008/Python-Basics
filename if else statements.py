marks=int (input("marks is : "))

if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >=70 and marks < 80):
    print("C")
else:
    print("D")

food = input("food : ")
eat = "Yes" if food == "cake" else "no"
print(eat)

food = input("food is: ")
print("sweet") if food == "cake" or food == "ice cream" else print ("not sweet")

age= int(input("age : "))
vote= ("yes","no") [age >= 18 ]

