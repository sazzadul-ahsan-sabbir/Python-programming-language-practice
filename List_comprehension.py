student=[
    {"name":"sazzad","marks": 80,"dept":"CSE"},
    {"name": "Karim","marks": 42,"dept":"EEE"},
    {"name": "Rafi","marks": 78,"dept": "CSE"},
    {"name": "Nabila","marks": 33,"dept": "BBA"},
    {"name": "Tania","marks":91,"dept": "CSE"},
]
passed_student=[s["name"] for s in student if s["marks"]>40]
print("Passed student:",passed_student)

cse_student=[s["name"]for s in student if s["dept"]=="CSE"]
print("cse stdents:",cse_student)

highest_mark=max(s["marks"] for s in student)
print("highest marks:",highest_mark)

lowest_mark=min(s["marks"] for s in student)
print("lowest marks:",lowest_mark)

# Grade feature
grades=[
    "A" if s["marks"]>=80
    else "B" if s["marks"]>=60
    else "C" if s["marks"]>= 50
    else "D" if s["marks"]>=40
    else "F"
    for s in student
]
print("Grades:",grades)

#Failed record

failed_student=[{"name":s["name"],"dept": s["dept"]}  for s in student if s["marks"]<40]
print("Failed student:",failed_student)

#Topper record

topper_student=[{"mame":s["name"],"dept": s["dept"]} for s in student if  s["marks"]==highest_mark
                ]
print("Topper student:",topper_student)