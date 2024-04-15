def finalGPA():

# Declare the point value for each letter grade
  A = 4
  B = 3
  C = 2 
  D = 1
  F = 0

# Collect information about the amount of credit hours for each class from user, then store in a variable
  creditHours = float(input("Enter the number of credit hours per course:"))

# Collect the number of courses completed by student, then store in variable
  coursesCompleted = int(input("Enter the number of courses completed:"))
  
# Collect the amount of each letter grades the user has recieved, (F = 0)
  gradeA = int(input("Enter the number of A's achieved:"))
  gradeB = int(input("Enter the number of B's achieved:"))
  gradeC = int(input("Enter the number of C's achieved:"))
  gradeD = int(input("Enter the number of D's achieved:"))

# Calculate the total possible credit hours, then store in variable
  totalPossibleCreditHours = creditHours * coursesCompleted

# Figure out total credit points earned by multiplying 'totalCreditPoints' by 'totalPossibleCreditHours' then divide by 'coursesCompleted'
  totalCreditPoints = (gradeA * A + gradeB * B + gradeC * C + gradeD * D) * totalPossibleCreditHours / coursesCompleted

# Calculate actuall GPA by dividing 'totalCreditPoints' by 'totalPossibleCreditHours'
  calculateGPA = totalCreditPoints / totalPossibleCreditHours

  print(f'Your grade point average is {calculateGPA}')

  return finalGPA


finalGPA()


# def calculateGPA():
#     # Map grades to their point values
#     grade_points = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

#     # Collect information about the amount of credit hours for each class from user
#     credit_hours_per_course = int(input("Enter the number of credit hours per course:"))

#     # Collect the number of courses completed by student
#     courses_completed = int(input("Enter the number of courses completed:"))
    
#     # Collect the amount of each letter grades the user has received
#     grade_counts = {}
#     for grade in grade_points.keys():
#         grade_counts[grade] = int(input(f"Enter the number of {grade}'s achieved:"))

#     # Calculate the total possible credit hours
#     total_possible_credit_hours = credit_hours_per_course * courses_completed

#     # Calculate the total credit points earned
#     total_credit_points = sum(grade_counts[grade] * grade_points[grade] for grade in grade_counts)

#     # Calculate the actual GPA
#     calculated_gpa = total_credit_points / total_possible_credit_hours

#     print(f'Your grade point average is {calculated_gpa}')

#     return calculated_gpa

# # Call the function
# calculateGPA()
