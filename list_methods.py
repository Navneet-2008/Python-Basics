# list= [2,1,3]
# list.append(4) #adds one element at the end [2,3,1,4]
# list.sort() #sorts in ascending order [1,2,3]
# list.sort(reverse=true) #sorts in descending order [3,2,1]
# list.reverse() #reverses list [3,1,2]
# list.insert(idx.el) #insert element at index 
# list.remove(1) #removes first occurence of the element [2,3,1]
# list.pop(idx) removes element at idx

list= ["c", "a", "k", "n" ,"y"]
# list.append(4)
# print(list)
list.sort()
print(list)
list.reverse()
print(list)

list2=[4,3,2]
list2.insert(0,5)
print(list2)

list3=[1,2,3]
list3.remove(2)
print(list3)

listt=[1,2,3,4,5,5]
listt.pop(3)
print(listt)

#practice question
list4=[]
mov=input("first movie: ")
list4.append(mov)
mov2=input("second movie: ")
list4.append(mov2)
mov3=input("third movie: ")
list4.append(mov3)

print(list4)

list1=[1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()

if(list1==copy_list1):
    print("palindrome")
else:
    print("not palindrome")

listtt=["C","D","A","A","B","B","A"]
listtt.sort()
print(listtt)