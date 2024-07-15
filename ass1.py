n=int(input("enter total number of student: "))
marks=[]
num_absent_std=0
total_marks=0
print("enter maks of student")

for i in range(n):
    x=int(input())
    if(x<0):
        num_absent_student_std+=1
    else:
        marks.append(x)
        total_marks+=x
max_marks=max(marks)
min_marks=min(marks)
avg_marks=(total_marks)/n
passed_student=0

for i in marks:
    if i>40:
        passed_student+=1
perpas=(passed_student/n)*100
perfail=((n-passed_student)/n)*100
highest_freq=0

a=0
marks.sort()

for i in range(n):
     if(marks.count(marks[i])>a):
        highest_freq=marks[i]
        a=marks.count(marks[i])


print("Average score is ",avg_marks)
print("Highest score is ",max_marks,"lowest score is ",min_marks)
print("Number of absentees is ",num_absent_std)
print("Marks with highest frequency is ",highest_freq)
print("percentage of students passed is ",perpas,"and fail is ",perfail)

