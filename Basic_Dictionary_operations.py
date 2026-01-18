#creating a dictionary
student={
    "Name":"Jony",
    "age":25,
    "grade":"A",
    "subjects":["Math","Physics","Chemistry"]
}
#Accessing values
print("Student Name:",student["Name"])
print("Student Age:",student["age"])

#Adding a new key-value pair
student["Country"]="Bangladesh"
print("student Country:",student["Country"])

#updating values
student["age"]=20
print("updated Age:",student["age"])

#removing a key-value pair
remove_grade=student.pop("grade")
print("Remove grade:",remove_grade)

