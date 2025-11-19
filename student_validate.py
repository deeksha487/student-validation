import sys
if len(sys.argv)!=5
    print("usage:student validate.py <name> <reg_no> <email> <dept>")

name=sys.argv[1]
reg_no=sys.argv[2]
email=sys.argv[3]
dept=sys.argv[4]

valid = True

if not reg_no.isdigit():
    print("Invalid registration number ,please enter the correct registration number:")
    valid = False

if "@" not in email:
    print("Invalid email ,please enter valid email id")
    valid = False

if valid:
    print("Registration successful")
    print("Student Name:",name)
    print("Student Register Number",reg_no)
    print("Email:",email)
    print("Department:",dept)
else:
    print("name:",deeksha)  
    print("reg_no:",62)  
    print("email:",deeksha@11)
    print("dept:",bca)
