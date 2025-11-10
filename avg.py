# Take input for 5 subject marks
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
sub4 = float(input("Enter marks for subject 4: "))
sub5 = float(input("Enter marks for subject 5: "))

# Calculate total and average
total = sub1 + sub2 + sub3 + sub4 + sub5
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
