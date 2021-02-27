#This is a variable for cars available
cars = 100
#This is a variable for the amount of space in a car
space_in_car = 4
#This variable is for the amount of drivers on hand.
drivers = 30
#This variable is for the number of passangers
passengers = 90
#This variable calculates how many cars are not being driven based on the number of drivers
cars_not_driven = cars - drivers
#This calculates the numbers of cars driven based on the number of drivers. Note that it makes the assumption that there are more cars than drivers.
cars_driven = drivers
#This calculates the amount of capacity we have for carpooling based on the amount of cars being driven.
carpool_capacity = cars_driven * space_in_car
#This will calculate how many passengers will fit into each carpool car.
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")