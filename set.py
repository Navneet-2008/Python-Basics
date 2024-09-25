a = {"hello",3,1,2,3,3,3, "abc"}
print(a)
print(type(a))
print(len(a))
#empty set ; syntax
a = set()

#set methods
#set.add(el) #adds an element
#set.remove(el) #removes the element 
#set.clear() #empties the set
#set.pop() #removes a random value
#set.union(set2) #combines both set values and returns new
#set.intersection(set2) #combines common values and returns new 

a = set()
a.add(3)
a.add(8)
a.add(8)
a.remove(3)
a.clear()
print(len(a))

set = {"hello", "world", "python"}
print(set.pop())

set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))

#practice question
subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(subjects))

marks={}

x = int(input("enter phy : "))
marks.update({"phy" : x})

y = int(input("enter maths : "))
marks.update({"maths" : y})

z = int(input("enter chem : "))
marks.update({"chem" : z})

print(marks)

values={9,"9.0"}
print(values)


