#Larry Hurley
#10-11-23
#Create & Call a function


def leap_year_calc(input_year):
    
    is_leap_year = False




    if (input_year % 4) == 0:      # inputYear is divisible by 4

      if (input_year % 100) == 0:   # inputYear is divisible by 100 (century year)

        if (input_year % 400) == 0: # inputYear is divisible by 400

          is_leap_year = True

        else:           # inputYear is not divisible by 400

          is_leap_year = False

      else:             # inputYear is not divisible by 100

        is_leap_year = True

    else:               # inputYear is not divisible by 4

      is_leap_year = False

        
    if is_leap_year:
        return True

    else:
        return False

#Main function will start here
def main():
    input_year = int(input("Enter a year: "))
    result = leap_year_calc(input_year)
    print(result)
    if result == True:
        print(f"{input_year}is a leap year")
    else:
         print(f"{input_year}is not a leap year")

#Call the main function
main()
