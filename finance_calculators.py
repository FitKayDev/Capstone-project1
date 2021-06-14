import math

#creating an investment calculator and a home loan repayment calculator
#user inputs their preferred calculator
print("Choose either 'investment' or 'bond' from the menu below.")
choice = input("Investment: \t- to calculate the amount of interest you'll earn on investment." +
                "\nBond: \t\t- to calculate the amount you'll pay on a home loan. ").title()

#output if user choice is interest or bond
if choice == "Investment":
    print("You have selected the Investment calculator.")

    #ask user to input initial amount, rate %, time period and the type of interest 
    invest_type = input("Please select the type of investment 'simple' or 'compound': ").lower()
    initial = int(input("Please enter the amount you are depositing: "))
    rate = int(input("Please enter the interest rate(only the numerical value): "))
    years = int(input("How many years do you plan to invest for: "))
    r = rate / 100

    #output is the calculated total simple or compound interest
    #simple interest A = P(1 + r * t) and compund interest A = P(1 + r)**t
    if invest_type == 'simple':
        simple = initial * (1 + (r)*years)
        print(f"Your simple interest total over {years} years at {rate}% is R{round(simple, 2)}.")
    elif invest_type == 'compound':
        compound = initial * math.pow((1+r), years)
        print(f"Your compound interest total over {years} years at {rate}% is R{round(compound, 2)}.")
    else:
        print("Please enter valid investment type, either 'simple' or 'compound'.")
elif choice == "Bond":
    print("You have selected the Bond calculator.")
    
    #bond repayment x = (i*P)/(1 - (1+i)**(-n))
    #user asked to input the value of house, rate % and the number of months for repayment
    value = int(input("Please enter the current value of the house: "))
    interest = int(input("How much is the interest rate(only numerical value): "))
    months = int(input("How many months do you plan to take to repay the bond: "))
    i = (interest / 100) / 12

    bond = (i*value)/(1 - (1+i)**(- months))
    print(f"You have to pay R{round(bond, 2)} each month for {months} months at {interest}%.")
else:
    print("Please enter 'investment' or 'bond'.")