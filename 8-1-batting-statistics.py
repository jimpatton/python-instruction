print("Welcome to the Batting Average Calculator")
choice = "y"
while choice == "y".lower():
    at_bat = 0
    while True:
        at_bat_input = int((input)("\nEnter number of times at bat: "))
        try:
            at_bat = int(at_bat_input)
            if at_bat < 1 or at_bat > 30:
                print("Error! Please enter a number between 1 and 30")
            else:
                break
        except ValueError:
            print("Please enter a valid number between 1 and 30")
    stats = [0] * at_bat
    print("\n0 = out, 1 = single, 2 = double, 3 = triple, 4 = home run")
    for i in range(at_bat):
        while True:
            result_input = int(input(f"Result of at bat {i+1}: "))
            try:
                result = int(result_input)
                if result <0 or result > 4:
                    print("Error! Please enter a number between 0 and 4")
                else:
                    stats [i] = result
                    break;
            except ValueError:
                print("Please enter a valid number between 0 and 4")
    hits = 0
    bases = 0
    for stat in stats:
        bases += stat
        if stat>0:
            hits += 1
    batt_avg = hits/at_bat
    slug_pct = bases/at_bat   
    print(f"\nBatting average: {batt_avg:.3f}")  
    print(f"Slugging percent: {slug_pct:.3f}")
    choice = input("\nAnother player? ") 