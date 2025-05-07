print("Sales Report")
sales =	[
	[ 1540.0, 2010.0, 2450.0, 1845.0 ], 
	[ 1130.0, 1168.0, 1847.0, 1491.0 ],
	[ 1580.0, 2305.0, 2710.0, 1284.0 ], 
	[ 1105.0, 4102.0, 2391.0, 1576.0 ] 
]
sum = 0.0
print("\nRegion\t\tQ1\t\tQ2\t\tQ3\t\tQ4")
for i in range (len(sales)):
    row = f"Region {i+1}\t"
    for j in range (len(sales[i])):
        row += f"${sales[i][j]:.2f}\t\t"
    print(row)
print("\nSales by Region")
for i in range(len(sales)):
    sum = 0.0
    for j in range (len(sales[i])):
        sum += sales [i][j]
    print(f"Region {i+1}\t${sum:,.2f}")
print("\nSales by Quarter")
for i in range (len(sales)):
    sum =0.0
    for j in range (len(sales[i])):
        sum += sales [j][i]
    print(f"Quarter {i+1}\t${sum:,.2f}")
for i in range (len(sales)):
    for j in range (len(sales[i])):
        sum += sales[i][j]
print(f"\nTotal Sales ${sum:,.2f}")    