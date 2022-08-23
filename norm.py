number = int(input("number of bikes you want to rent: "))
duration = int(input('how long do you want to rent the bike for(""): '))
nemb = input('please enter d for days and h for hours for rent duration')
costDaily = number * duration * 20
costHourly = number * duration * 5

if duration or number <= 0:
    print('please select a valid number ("it must be a positive integer!! ")')
else:
    if nemb != 'h' or 'd':
        print('you did not select a valid unit for the rental period please choose again')

    elif nemb == 'h':
        print("the cost of renting the bike for " + str(duration) + "hrs is going to be " + str(costHourly))
    else:
        print("the cost of renting the bike for " + str(duration) + "day is going to be " + str(costDaily))
