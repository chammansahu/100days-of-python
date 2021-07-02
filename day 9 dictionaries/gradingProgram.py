students={
    "Ram":99,
    "Balram":89,
    "Sudama":90,
    "Bharat":94,
    "Shyma":95,
}
student_grades={}

for student in students:
    score = students[student]
    if score  >= 90:
        student_grades[student]="A"
    elif score >= 80:    
        student_grades[student] ="B"
    elif score >= 70:    
        student_grades[student] ="C"
    elif score >= 50:    
        student_grades[student] ="D"
    else:
        student_grades[student] = "F"
        
print(student_grades)    
