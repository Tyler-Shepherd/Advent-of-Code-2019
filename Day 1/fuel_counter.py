inputs = open("./fuel.txt", "r")

line = inputs.readline()

total_fuel = 0

while line:
	mass = line
	fuel_needed = int(mass) // 3 - 2

	total_fuel += fuel_needed


	line = inputs.readline()

print(total_fuel)