print("Welcome to Average height calculator")

student_heights = input("Input a list of student heights ").split(" ")

number_of_students = 0
for i in student_heights:
    number_of_students += 1

sum_of_height = 0
for i in range(0, number_of_students):
    student_heights[i] = int(student_heights[i])
    sum_of_height += student_heights[i]

average_height = sum_of_height / number_of_students

print(f"Average height: {average_height}")
