print("Welcome to the High score finder !!")

student_scores = input("Please enter a list of student scores: ").split()

for student_score in range(0, len(student_scores)):
  student_scores[student_score] = int(student_scores[student_score])

print(student_scores)
# print(max(student_scores))
# print(min(student_scores))

max_score = 0
for score in student_scores:
  if score > max_score:
    max_score = score
print(max_score)

  


