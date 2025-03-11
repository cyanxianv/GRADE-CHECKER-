assign_grade = int(input("What is your grade? Enter your score (0-100):"))

if assign_grade > 100:
	print(f"{assign_grade}? That's over 100. Try again with a score between 0 and 100.")
elif assign_grade >= 90:
	print(f"{assign_grade} gets you an A. Nice work, keep it up!!")
elif assign_grade >= 80:
	print(f"{assign_grade} is a B. Solid effort, you did well")
elif assign_grade >= 70:
	print(f"{assign_grade} means a C.Try a bit more, i know you can do it!!")
elif assign_grade >= 60:
	print(f"{assign_grade} is a D. Maybe study more, you can still improve.")
elif assign_grade >= 0:
	print(f"{assign_grade} is an F. You need to study. seriously")
else:
	print(f"{assign_grade}? Negative Scores dont work. Use 0 to 100")							