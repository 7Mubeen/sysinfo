students = {
    'Mubeen': 78,
    'Hamza': 92,
    'Ali': 85,
    'Sara': 96,
    'Usman': 88
}
count = 0
marks = 0
#highest_scorer , score = list(students.items())[0]
total_student = len(students)
print(total_student)
for key, values in students.items():
	marks =	marks + values
print("Marks: ",marks)
avg = marks / total_student
for key, values in students.items():
	if values > avg:
		count = count + 1
print("Student above average: ", count)
print("Average score: ",avg)
#for key, value in students.items():
#	if value <  score:
#		score = value
#		highest_scorer = key
#print("Highest scorer: ",highest_scorer)
#print("Score: ",score)
#student = {
#    'name': 'Mubeen',
#    'age': 19,
#    'country': 'Pakistan',
#    'goal': 'Python Developer'
#}
#if 'goal' in student:
#	print("Goal is exist")
#else:
#	print("Goal does not exist")
#student['goal'] = 'ML Engineer'
#student['age'] = 19
#for key, value in student.items():
#	print(key, ":", value)
#print(student['name'])
#if 'goal' in student:
#	print('goal', ":", student['goal'])
#if 'Python' in student.values():
#	print("Python found")
#else:
#	print("Python not found")
#found =False
#for value in person.values():
#	if value == 'Pakistan':
#		found = True
#if found:
#	print("Pakistan found")
#else:
#	print("Pakistan not found")
#for value in person.values():
#	print(value)
#person = {
#    'name': 'Mubeen',
#    'age': 18,
#    'country': 'Pakistan'
#}
#print(person['name'])
#new_age = person['age'] + 1
#person['age'] = new_age
#person['goal'] = 'ML Engineer'
#if 'country' in person:
#	print("Country exists")
#print(person)
#person = {'name': 'Mubeen', 'age': 18, 'country': 'Pakistan'}
#for key, value in person.items():
#	if key == 'age':
#		new_age = person['age'] + 1
#		person['age'] = new_age
#		print(person['age'])
#for key, value in person.items():
#	if value == 'Pakistan':
#		print(key,":", value)
#person.pop('country')
#country = 'name'
#for key, value in person.items():
#	if value == 'Mubeen':
#		print("Mubeen is stored under the key:", key)
#print("-----")
#for key in person:
#	print(key,":", person[key])
#print("----")
#for key in person:
#	print(person[key])
#if 'country' in person:
#	print(person[country])
#else:
#	print("Country information not avaliable")
#print("Initial number of information: ", len(person))
#person['goal'] = 'ML Engineer'
#person['age'] = '19'
#person.pop('country')
#removed_goal = person.pop('goal')
#if 'age' in person:
#	print("Age exist")
#else:
#	print("Age don't exist")
#print("Name: ",person['name'])
#print("Age: ",person['age'])
#print("Country: ",person['country'])
#print("Removed goal: ",removed_goal)
#print("Final number of information", len(person))
