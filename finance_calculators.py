import math

# first output shown to the user
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print("Enter 'investment' or 'bond' from the menu above to proceed: ")

# get user input
calculation_type = input().lower()

# check user input using if
if calculation_type == "investment":
    # get investment details
    deposit = float(input("Enter the amount of money you are going to deposit: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter how many years you plan on investing: "))
    interest = input("Do you want 'simple' or 'compound' interest? ").lower()

    # calculate interest
    if interest == "simple":
        total = deposit * (1 + (interest_rate * years))
    elif interest == "compound":
        total = deposit * math.pow((1 + interest_rate), years)
    else:
        print("Invalid input. Please enter simple or compound.")
        exit()

    # print result - use round() to make it look nicer
    print("Total amount after {} years: R{}".format(years, round(total, 2)))

elif calculation_type == "bond":
    # get bond details
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: ")) / 100
    months = int(input("Enter the number of months to repay the bond: "))

    # repayment calculation
    i = (interest_rate / 12)
    repayment = (i * present_value) / (1 - math.pow((1 + i), -months))

    # display result
    print("Monthly repayment: R{}".format(round(repayment, 2)))

else:
    print("Invalid input. Please enter investment or bond.")