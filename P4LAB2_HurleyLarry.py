#Larry Hurley
#10/4/23
#Intro to loops using range ()

int_1 =  int(input(' enter a number '))
int_2 =  int(input(' enter a number '))
# If first # is smaller 
if int_1 <= int_2:
    #Execute for loop using range (start,stop,step)
    for x in range ( int_1, int_2 + 1, 5):
        print (x)
else:
    print( " The first number must be smaller.")
