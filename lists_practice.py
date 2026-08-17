students = ["Ali", "Sara", "Mubeen", "Hamza", "Usman"]
print("Number of student: ", len(students))
for student in students:
	if student == "Sara":
		print("Sara is in the list")
removed_student = students.pop(4)
print("Removed student: ", removed_student)
students.remove("Sara") 
print("Final students: ",students)
print("Final number of students: ",len(students))
