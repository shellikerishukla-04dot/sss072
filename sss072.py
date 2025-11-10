# Take input for 5 subject marks
s1 = float(input("Enter marks for subject 1: "))
s2 = float(input("Enter marks for subject 2: "))
s3 = float(input("Enter marks for subject 3: "))
s4 = float(input("Enter marks for subject 4: "))
s5 = float(input("Enter marks for subject 5: "))

# Calculate total and average
total = s1 + s2 + s3 + s4 + s5
average = total / 5

# Determine grade based on average
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print results
print(f"\nTotal marks = {total}")
print(f"Average marks = {average:.2f}")
print(f"Your grade is: {grade}")
