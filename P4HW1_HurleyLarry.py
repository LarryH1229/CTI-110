#Larry Hurley
#10-9-23
#

def num_to_letter(number):

  if number <= 100 and number >=90:

    letter = "A"

  elif number <= 89 and number >=80:

    letter = "B"

  elif number <= 79 and number >=70:

    letter = "C"

  elif number <=69 and number >=60:

    letter = "D"

  else:

    letter = "F"

  return letter


num_grades = int(input("How many grades will you enter?"))

#Create an empty list
grades_list = []

#Create a loop to enter the scores 
for value in range(num_grades):    #What will the variable value output
    grade = int(input(f"Enter grade #{value + 1}): "))
    if grade >= 0 and grade <= 100:
            grades_list.append(grade)
    else:
        while grade < 0 or grade > 100:
            print(" INVALID GRADE ENTERED!")
            print("Grade should be between 0 and 100")
            grade = int(input(f"Re-enter grade # {value+1}:"))
        grades_list.append(grade)

min_grade = min(grades_list)

grades_list.remove(min_grade)

adverage = (sum(grades_list))/len(grades_list)

print(" --------Results-----")
print("The lowest grade is:",min_grade)
print(f'Grade after dropping lowest {grades_list}')
print(f"Adverage: {adverage}")
print(f"Letter Grade: {num_to_letter(adverage)}:")
            
