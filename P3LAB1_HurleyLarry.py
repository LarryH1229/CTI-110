#Larry Hurley
#10/2/23
#Using IF statements to determine leap year

#Get unput from user

input_year = int(input(" enter a year"))

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print("the year is a leap year")

        else:
            print(" The year is NOT a leap year")

    else:
        print(" The year is a leap year")

else:
    print(" The year is NOT a leap year")
