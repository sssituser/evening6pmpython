students =dict()
print(students,type(students))
students[1] = "kiran"
students[2] = "jaswanth"
students[3] = "Murthy"
students[4] = "Ahmed"
students[5] = "sirisha"
students[5] = "Raj"
print(students)

for item in students.items():
    print(item)
print("keys in the dictonary")
for k in students.keys():
    print(k)
print("Values in the dictonary")
for v in students.values():
    print(v)
