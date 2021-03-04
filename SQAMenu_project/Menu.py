#declarations
height = ""
weight = ''
age = ''

def calculator():
    print("1 - Body Mass index 2 - Retirement 3 - Exit Program ")
    answer = input("INPUT 1, 2 or 3  ")

    #Body Mass Index
    if (answer == '1'):
        height_1 = int (input("Height(FEET) ")) #
        height_2 = int(input("HEIGHT(INCHES)"))
        final_height = (height_1 * 12) + height_2

        #print(height_1)
        #print(height_2)
        #print(final_height)
        weight = int (input ("what is your weight "))# needs to be lbs only

        #calculate BMI
        BMI = 703 * weight / (final_height * final_height)
        rounded_BMI = round(BMI, 1) #rounds BMI 1 digit
        #print(rounded_BMI)

        #How good your BMI is catigorized
        if rounded_BMI <= 18.5:
            print("You are underweight")
            calculator()  # run function again
        if (rounded_BMI >= 18.5) and (rounded_BMI <= 24.9):
            print("You are Normal Weight")
            calculator()  # run function again
        if (rounded_BMI >= 25) and (rounded_BMI <= 29.9):
            print("You are Overweight")
            calculator()  # run function again
        else:
            print("You are Obese")
        calculator() # run function again


    #Retirement
    if (answer == '2'):
        age = int (input("Age "))
        print(age)
        salary = int (input("Salary "))
        print(salary)
        percentage_saved = float (input("Percentage Saved "))
        print(percentage_saved)
        savings_goal = int (input("Savings Goal "))
        print(savings_goal)


        #calculate Retirement
        age_when_hit_1 = (salary * percentage_saved)  * 1.35
        age_when_hit_2 = savings_goal / age_when_hit_1
        final_age_hit = age + age_when_hit_2

        #round Final_age_hit
        rounded_FAH = round(final_age_hit, 0)

        # output when savings goal will be hit
        if rounded_FAH <= 99: # less than 100
            print(rounded_FAH, "years old ")
        else:
            print("Savings goal not met")


        calculator()

    #exit the program
    if (answer == '3'):
        print("exiting the program")
        exit()

    else:
        print("incorrect, input 1 2 or 3 no spaces")
        calculator()

calculator()

# bmi calculation Formula: 703 x weight (lbs) / [height (in)]^2 *** works

