import pandas as pd
import random

# Create fictional data
departments = ["Computer Science", "Cybersecurity", "Software Engineering", "Information Technology", "Data Science" ]
level = [100, 200, 300, 400]

data = []
for i in range(1, 51): #50 students
    student_id = f"STU{1000 + i}"
    dept = random.choice(departments)
    level = random.choice(levels)
    attendance = round(random.uniform(60, 100), 1)
    avg_score = round(random.uniform(45, 95), 1)
    data.append([student_id, dept, level, attendance, avg_score])

df = pd.DataFrame(data, columns=["Student_ID", "Department", "Level", "Attendance_Percentage", "Average_Examination_Score"])
df.to_csv("student_dataset.csv" , index=False)
print(df.head(10)) # show first 10 rows
print("\nDataset saved as student_dataset.csv")