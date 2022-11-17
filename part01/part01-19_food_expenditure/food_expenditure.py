times_eating_lunch = int(input("How many times a week do you eat at the student cafeteria? "))
price_of_lunch = float(input("The price of a typical student lunch? "))
money_spent_on_groceries = float(input("How much money do you spend on groceries in a week? "))

weekly = (times_eating_lunch * price_of_lunch) + money_spent_on_groceries

print("Average food expenditure:")
print(f"Daily: {weekly / 7} euros")
print(f"Weekly: {weekly} euros")