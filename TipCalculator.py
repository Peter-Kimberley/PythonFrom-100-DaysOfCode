"""The following is a tip calculator"""


totlaOfTheBill = float(input("What was the total amount of the bill? "))

splitBetweenHowMany = int(input\
                          ("How many people are splitting the bill? "))


tip = float(input("How much of a tip would you like to leave? "))


"""This is the actual calculation for the total to pay
including the tip"""
amountToPayPerPerson = (totlaOfTheBill /splitBetweenHowMany * tip)

"""This will calculate the price too 2 decimal places"""
amountToPayPerPerson = float(amountToPayPerPerson)

print("The total amount to pay is " + str(round(amountToPayPerPerson, 2)))
