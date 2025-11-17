import sys

if len(sys.argv) < 2:
    print("Please provide a string as an argument.")
    sys.exit()

text = sys.argv[1]

if text == text[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
