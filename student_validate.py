import sys

if len(sys.argv) != 5:
    print("usage: student_validate.py <name> <reg_no> <email> <dept>")
    sys.exit()

    name = sys.argv[1]
    reg_no = sys.argv[2]
    email = sys.argv[3]
    dept = sys.argv[4]
    
valid=true
if not reg_no is digit():
    print("invalid registration")
    
if @ not in email():
    print("please enter the correct email id")


if valid:
    print("Registration successful!")
    print("student name:",name)
    print("Student Registration number:", reg_no)
    print("Email:", email)
    print("Department:", dept)
else:
    print("name:", "deeksha")
    print("email:",deeksha@11)
    print("reg_no:", 62)
    print("dept:", "bca")
