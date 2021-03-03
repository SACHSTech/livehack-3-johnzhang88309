"""
--------------------------------------------------------
Name: Group calculator.py
Purpose: Asks the user for wins and losses and outputs what group they are in
 
Author: Zhang.J 
 
Created:  date in 03/03/2021
--------------------------------------------------------
"""

print ("***** Tournament Tracker *****")

#create for loop to ask the user for wins and losses
print("")
total = 0
for i in range (6):
  win_or_loss = input ("Win or Loss (write W for wins and L for losses): ")
  if win_or_loss == "W":
    total = total + 1

print("")

#calculations and final print statement
if total == 0: 
  print ("You are eliminated from the tournament")  
elif total == 1 or total == 2:
  print ("You are placed in group 3")
elif total == 3 or total == 4:
  print ("You are placed in group 2")  
else: 
  print ("You are placed in group 1")



