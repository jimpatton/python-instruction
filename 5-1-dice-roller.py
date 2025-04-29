print("Dice Roller")
choice = "y"
while choice.lower() == "y":
    import random
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    total = d1 + d2
    print(f"Total: {total}")
    if total == 2:
        print("Snake eyes!")
    elif total == 7:
        print("Craps!")
    elif total == 12:
        print("Boxcars!")
    choice = (input("\nRoll again? "))
