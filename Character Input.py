# Application will prompt user for name and age
# Returns the year that user turns 100 years old
from datetime import datetime


# logic to calculate the year user turns 100, including error handling
def cal_100_yrs(info):
    try:
        year_at_100 = (100 - int(info[1])) + datetime.now().year
        print(f"\n{info[0]} will turn 100 years old in the year {year_at_100}.")
    except ValueError:
        print("Invalid input. Try again.")


# loops program until user quits
while True:
    name = input("\nEnter your name, or type 'exit' to quit: \n")
    if name == "exit":
        break
    else:
        age = input("Enter your age, or type 'exit' to quit: \n")
    if age == "exit":
        break
    else:
        name_age_list = (name, age)
        cal_100_yrs(name_age_list)
