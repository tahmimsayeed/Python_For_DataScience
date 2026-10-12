marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]
grand_counts={}
valid_marks=[]
average = 0
for mark in marks:
  if mark>=0 and mark<100:
    valid_marks.append(mark)

for mark in valid_marks:
    if mark<=0 and mark>100:
        continue
    elif mark>= 80:
        grade = "A"
    elif mark >=70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"
    
    grand_counts[grade] = grand_counts.get(grade,0)+1
    average = sum(valid_marks)/len(valid_marks)
print(f"Valid marks: {valid_marks}")
print(f"Grade counts: {grand_counts}")
print(f"Average: {average}")

