# Attendance Management System

attendance = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    status = input("Present(P) / Absent(A): ").upper()
    attendance[name] = status

print("\nAttendance Report")
print("------------------")

present = 0

for name, status in attendance.items():
    print(name, ":", status)
    
    if status == "P":
        present += 1

percentage = (present / n) * 100

print("\nTotal Students =", n)
print("Present Students =", present)
print("Absent Students =", n - present)
print("Attendance Percentage =", percentage, "%")