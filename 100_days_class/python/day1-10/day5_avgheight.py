student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


lenth = len(student_heights)
total = sum(student_heights)
avg = round(total / lenth)

print(int(avg))
