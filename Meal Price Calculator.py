child_meal_cost = float(input("What is the price of a child's meal: "))
adult_meal_cost = float(input("What is the price of an adult's meal: "))
child_count = int(input("How many children are there? "))
adult_count = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))
print()
subtotal = float(child_meal_cost*child_count) + (adult_meal_cost*adult_count)
print("Subtotal: " + str(subtotal))
