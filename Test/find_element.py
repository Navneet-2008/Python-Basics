# find whether an element x exists in a tuple or not
# if x exists print YES otherwise NO
tuple = (23, 65, 55, 11, 26, 97, 45)
x = int(input("Enter x: "))

present = False
for item in tuple:
    if(item == x):
        present = True

if(present == True):
    print("YES")
else:
    print("NO")

