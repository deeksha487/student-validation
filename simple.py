# Simple Interest Calculator

# Taking user input
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of Interest: "))
time = float(input("Enter the Time period (in years): "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Displaying result
print("Simple Interest =", simple_interest)
