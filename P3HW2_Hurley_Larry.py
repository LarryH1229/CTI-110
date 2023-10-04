#Larry Hurley
#10-4-23
#Use if else statements to determine gross pay

#Step 1 Get input from the user
name= input("Enter employee name: ")
num_hours = float(input("Enter number of hours worked:"))
pay_rate = float(input("Enter the hourly pay rate:"))
OT_hours = 0
has_OT = False
OT_pay = 0
reg_pay = 0
#Step 2Calculate overtime = yes/no - how much
if num_hours > 40:
    has_OT = True
    OT_hours = num_hours - 40
else:
    has_OT = False

if has_OT == True:
    OT_pay = (pay_rate*1.5) * (num_hours - 40)#Actucal OT total pay
else:
    OT_pay = 0
    
#Calculate regular pay
reg_pay = pay_rate * num_hours - OT_hours

# Display name, pay rate, num hours worked,OT hours, OT pay,regular gross pay

print("Name:",name)
print("Overtime Hours:",OT_hours)
print("Overtime pay:",OT_pay)
print("Regular hours:",num_hours - OT_hours)
print("Regular pay:",reg_pay)
print("Gross pay:",reg_pay + OT_pay)
