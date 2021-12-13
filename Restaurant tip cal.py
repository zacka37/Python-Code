# Zack Augustine May 8th 2021
# Calculate the tip and the total bill amount
def main():
    agian_loop = True
    print("Restaurant Tip Calculator\n_________________________")
    while(agian_loop):
        
        try:
            bill_amount = float(input("What is the bill amount:$ "))
            enter_amount = int(input("Enter a percent: . "))
            
            turn_enter_amount_to_percent = enter_amount / 100 # Convert to percent
            tip = bill_amount * turn_enter_amount_to_percent # Calculate tip
            print("The tip is: ", tip, "\n")
            total_bill = bill_amount + tip  # Calculate total for bill + tip
            print("The bill toal is: ", total_bill)

            agian = input("Do you want to calculate another tip? (y/n): ")
            if agian != "y":
                agian_loop = False
        except ValueError:
            print("Enter only a number or a float")
main()
    
