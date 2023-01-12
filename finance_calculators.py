import math

print("""Investment - To calculate the amount of interest you'll earn on your investment.
Bond - to calculate the amount you'll have to pay on a home loan.\n """)

# gets user input for which calc they want
calc = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# collects user information for investment
if calc == "investment":
    deposit = float(input("How much money are you investing? "))
    interest_rate = float(input("What is the interest rate on this investment? "))
    years = int(input("How many years will you be investing? "))
    interest = input("Would you like simple or compound interest? ").lower()

    # uses information to calculate profit depending on interest type
    if interest == "simple":
        profit = deposit * (1 + (interest_rate/100) * years)
    else:
        profit = deposit * (1 + (interest_rate/100)) ** years

    print(f"\nUsing the information supplied, your expected profit will be £{profit - deposit:.2f}.")

# collects user information for bond
elif calc == "bond":
    house_val = float(input("How much is the house currently worth? "))
    house_annual = float(input("How much is the interest rate? "))
    months = int(input("How many months would you like to pay the loan back in? "))

    # calculates the monthly payment based on user input
    house_monthly = (house_annual / 100) / 12
    repayment = (house_monthly * house_val) / (1 - math.pow(1 + house_monthly, -months))

    print(f"\nUsing the information supplied, your monthly payments will be £{repayment:.2f}.")

# displays error if user input is not either bond or investment
else:
    print("Input error. Please enter either 'bond' or 'investment'.")

print("\nThank you for using the calculator.")
