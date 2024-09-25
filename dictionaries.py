info={
    "name":"navneet",
    "class":"XI D",
    "marks":88,
    "topics":["python","java","c"],
    "subjects":("sets","dictionary"),
    78:89.90,
}
info["surname"]="virdi"
print(info)

#nesting in dictionary
student={
    "name" : "nannu",
    "subjects" : {
        "phy":59,
        "chem":89,
        "math":60,
    }
}

print(student["subjects"]["chem"])

#mydict.keys() #returns all keys
#mydict.values() #returns all values
#mydict.items() #returns all (key,val) pairs as tuples
#mydict.get("keys") #returns the key according to value 
#mydict.update(newdict) #inserts the specified items to the dictionaries 

student={
    "name":"navneet",
    "subjects": {
        "phy":55,
        "chem":78,
        "maths":54,
    }
}
print(list(student.keys()))
print(student.keys())
print(len(student))
print(list(student.values()))
pairs=list(student.items())
print(pairs[1])
print(student.get("name"))
new_dict=({"city": "delhi" , "topic": "python"})
student.update(new_dict)
print(student)

#practice questions
info = {
    "table" : ["a piece of furniture" , "list of facts and figures"],
    "cat" : "a small animal",
}
print(info)
