def get_fuel_needed(mass):
	# print("get fuel of", mass)

	fuel_needed = mass // 3 - 2

	if fuel_needed <= 0:
		return 0

	additional_fuel = get_fuel_needed(fuel_needed)

	# print("for", mass, "needs", fuel_needed, "with additional", additional_fuel)

	return fuel_needed + additional_fuel



inputs = open("./fuel.txt", "r")

line = inputs.readline()

total_fuel = 0

while line:
	total_fuel += get_fuel_needed(int(line))

	line = inputs.readline()

print(total_fuel)