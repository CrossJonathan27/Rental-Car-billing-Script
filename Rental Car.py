import sys

#this code asks the user to input the rental code B, D, or W. as well as if the user inputs a lower case letter, changes it 
#to uppercase to match the code.
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n").upper()

#this block of code provides a loop wherein if the user inputs anything besides B, D, or W, it asks the user to re-enter the 
#correct code. It also ensures that when the correct input is entered, it stops the loop and proceeds to the next block of code.
while rentalCode not in ("W", "D", "B", "w", "d", "b"):
  print("rental code not valid, please re-enter the rental code.")
  rentalCode = input.upper("(B)udget, (D)aily, or (W)eekly rental?\n")
  if rentalCode in ("W", "D", "B"):
    break;
    
#this block of code say for each letter code is a seperate input depending on the code entered.
#for each letter, the variable changes based on what the user enters, and then the system asks for another variable entered by
#the user.
if rentalCode == "W":
  rentalPeriod = input("Number of weeks rented:\n");
elif rentalCode == "B":
  rentalPeriod = input("Number of Days Rented:\n");
elif rentalCode == "D":
  rentalPeriod = input("Number of Days Rented:\n");

#this block assigns the cost for each rental code. 
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00	

#this block indicates the different calculations for each rental code and assigns the solution to the variable baseCharge
#based on the input of the user.
if rentalCode == "B":
  baseCharge = int(rentalPeriod) * int(budget_charge)
elif rentalCode == "D":
  baseCharge = int(rentalPeriod) * int(daily_charge)
elif rentalCode == "W":
  baseCharge = int(rentalPeriod) * int(weekly_charge)

 #this block prompts the user to input the starting and ending mileage and assigns them to the variable odoStart and odoEnd. 
odoStart = input("Starting odometer reading:\n")
odoEnd = input("Ending odometer reading:\n")

#this block of code calculates the number of miles driven while the vehicle was rented
#and assigns the number to the variable totalMiles.
totalMiles = int(odoEnd) - int(odoStart)

#this code states that if the user inputs B for the rental code, then the mile charge is calculated.
if rentalCode == "B":
  mileCharge = float(totalMiles) * 0.25;

#this block of code states if the user inputs D as the rental code, then the average 
#day miles is calculated. if the average day miles is less than or equal to 100, then the #mile charge is 0. if it is more, 
#than 100 is subtracted from it, and the calculation of 
#.25 cents per mile times the number of days is calculated an assigned to the variable. 
#mileCharge.
elif rentalCode == "D":
  averageDayMiles = float(totalMiles)/float(rentalPeriod);
  if float(averageDayMiles) <= 100:
      extraMiles = 0;
  else:
      extraMiles = float(averageDayMiles) - 100;
  mileCharge = (.25 * float(extraMiles)) * float(rentalPeriod);

#this block of code states that if the user inputed W for the rental code, then the 
#average weekly miles is calculated. if the average weekly miles is less than or equal 
#to 900, the mile chwrge is 0.if it is more, the calculation of 100 times the number of #weeks rented is computed and assigned
# to the variable mile charge.
elif rentalCode == "W":
  averageWeekMiles = float(totalMiles)/ float(rentalPeriod);  
  if averageWeekMiles <= 900:
    mileCharge = 0;
  else:
    mileCharge = 100 * float(rentalPeriod);
    
#this code calculates the base charge + the mile charge and assigns it to the variable
#amtdue for the cost.
amtDue = float(baseCharge) + float(mileCharge)

#this block of code prints out a 'reciept' to the customer with a summary of charges.
print("Rental Summary")
print("Rental Code:       " + str(rentalCode))
print("Rental Period:         " + str(rentalPeriod)) 
print("Starting Odometer: " + str(odoStart))
print("Ending Odometer:   " + str(odoEnd))
print("Miles Driven:      " + str(totalMiles))
print("Amount Due:        " + "$" + str(amtDue) + '0')
