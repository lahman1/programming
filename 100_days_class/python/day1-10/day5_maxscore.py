student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_value = None

for num in student_scores:
    if max_value is None or num > max_value:
        max_value = num

print(f"The highest score in the class is: {max_value}")
