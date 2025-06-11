print("Split Bill Calculator")

bill = float(input("How much was the bill?\n"))
tip = int(input("How much is the tip percentage?\n"))
people = int(input("How many people are you going to divide it between?\n"))

# Calculate the tip amount
def calculate_tip_amount(bill, tip):
    return (tip / 100) * bill

tip_amount = calculate_tip_amount(bill, tip)

# Calculate the total bill including tip
def calculate_total_bill(bill, tip_amount):
	return bill + tip_amount

total_bill = calculate_total_bill(bill, tip_amount)

# Split the total bill by the number of people
def calculate_split_bill(total_bill, people):
	return total_bill / people
 
split_bill = calculate_split_bill(total_bill, people)

# Print the results
print(f"The final bill is ${total_bill:.2f}, which is ${split_bill:.2f} per person.")
