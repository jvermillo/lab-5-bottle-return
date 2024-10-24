# Juniper Vermillo
# CIS 129
# 10/24/2024
# Lab 5 - The Bottle Return Program
"Calculate the week's payout based on the number of bottles returned per day"

# Loop Control
keep_going = "y"

# Program Loop
while keep_going == "y":
    # Variables
    today_bottles = 0
    counter = 1
    total_bottles = 0
    total_payout = 0

    # Week's worth of data
    while counter <= 7:
        today_bottles = int(input(f"Enter the number of bottles for day #{counter}: "))
        total_bottles += today_bottles
        counter += 1

    # Calculating Payout
    total_payout = total_bottles * .10 # Payout per bottle

    # Results Display
    print(f"The total number of bottles collected is {total_bottles}.")
    print(f"The total paid out is ${total_payout:.2f}.")

    # Running the Program Again
    keep_going = input("Would you like to enter another week's worth of data? (y/n) ")
    while keep_going.lower() not in ["y", "n"]:
        keep_going = input("Invalid input. Select 'y' or 'n'. ")