"""
--------------------------------------------------------
Name: DoorDash Distance Tracker .py
Purpose: Tracking the first 100km driven and output the number of days it took and the average distance per day
 
Author: Zhang.J 
 
Created:  date in 03/03/2021
--------------------------------------------------------
"""

print("***** Welcome to the DoorDash Distance Tracker ******")

#variables 
total_distance = 0
days = 0 

#ask the user how far they drove until 100km
print("")
print ("** Travel Log** ")
print("")
while total_distance < 101: 
  distance_travelled = float(input("Enter the distance distance travelled for the day: "))
  total_distance = total_distance + distance_travelled
  days = days + 1 

print("")

#Calculations for days and average distance per day
average_distance = total_distance/days

print ("** Summary **")
print ("")
print ("It took " + str(days) + " days to surpass 100km driven")
print("The average distance driven per day is " + str(round(average_distance,2)) + " km")




