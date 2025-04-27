print("Welcome to the Tip Calculator")
choice ="y"
while choice == "y".lower():
    meal = float(input("\nCost of meal: "))
    for d in [.15,.20,.25]:
        tip = meal * d
        total = meal + tip
        print(f"\n{int(d*100)}%")
        print(f"Tip amount: ${tip:.2f}")
        print(f"Total amount: ${total:.2f}")
    