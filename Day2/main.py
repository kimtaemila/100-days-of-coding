#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tips = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = (total_bill * (tips / 100)) + total_bill
split_with_people = bill_with_tip / people
total_amount = round(split_with_people, 2)
total_amount = "{:.2f}".format(split_with_people)
print(f"Each person should pay ${total_amount}")