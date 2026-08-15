grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Emma": 88
}
total = 0
for score in grades.values():
    total += score
average = total / len(grades)
print("Class Average:", average)
highest_score = max(grades.values())
lowest_score = min(grades.values())
top_student = max(grades, key=grades.get)
bottom_student = min(grades, key=grades.get)
print("Top Scorer:", top_student, "-", highest_score)
print("Bottom Scorer:", bottom_student, "-", lowest_score)
student = input("Enter a student's name to look up their grade: ")
score = grades.get(student)
if score is not None:
    print(student, "scored", score)
else:
    print("Sorry, that student is not in the grade book.")