print("Welcome to the Travel Time Calculator")
choice = "y"
while choice == "y".lower():
    miles = int(input("\nEnter miles: "))
    mph = int(input("Enter miles per hour: "))
    time  = miles/mph
    hours = int(time)
    minutes = (time - hours)*60
    print("\nEstimated travel time")
    print("---------------------")
    print(f"Hours: {hours}")
    print(f"Minutes: {round(minutes)}")
    choice = input("\nContinue? (y/n): ")
    
    
