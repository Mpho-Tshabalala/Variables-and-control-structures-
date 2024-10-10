import math
 
# Inform the user of all the interest calcuation types are able to make when using the calculator
print("Which type of interest calculation would you like to make, your options are listed below: ")
print("-Investment (calculate the amount you will make on your investment) ")
print("-Bond (calculate the amount you will have to pay on your home loan) ")

# Now ask them to enter the type of interest they would like to calculate and convert the string into all lowercase letters
interest_type = input("Please enter the type of interest calculation you would like to make: ")
interest_type = interest_type.lower()



# Now write a if statement to decide whether or not the user entered the correct inputs and proceed
if (interest_type == "investment") or (interest_type == "bond"):
    
        # Ask the user for percentage of their interest rate
    raw_interest = int(input("Enter the interest rate (just write down the number without the percentage sign i.e 20): "))

    # Now turn the interest rate entered by the user into a percentage
    interest_rate = raw_interest/100
    
    #Proceed with action corresponding to the investment
    if interest_type == "investment":
    
        # Now ask the user for all the variables needed to calculate the total
        deposit_amount = int(input("What is the amount that you will be depositing (in Rands): "))
        years = int(input("Please enter the number of years that you will be investing for: "))
        interest = input("Will you be using simple or compound interest (simply enter simple or compound): ")
        interest = interest.lower()
        
        # Now calculate and print the total according to the specifications given by the user.
        if interest == "simple":
            total = str(deposit_amount*(1+interest_rate*years))
            print("The total for your investment is R" + total)
            
        else: 
            total = str(deposit_amount*math.pow((1+interest_rate),years))
            print("The total accumulated amount for your investment is R" + total)
            
    else:
        #Proceed with directions corresponding to the user choosing the bond option 
        present_value = int(input("What is the present value of the house (in Rands): "))
        interest = interest_rate/12
        months = int(input("Please enter the number of years that you will be paying the bond for: "))
        months = months*12
        
        #Now calculate and print the total according to the user inputs
        total = str((interest*present_value)/(1-(1+interest)**(-months)))
        print("The total interest you will be paying on your bond is R" + total)
        
else:
    print("You have entered an invalid input")
        
       