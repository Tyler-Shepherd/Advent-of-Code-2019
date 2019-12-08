inputs = open("./data.txt", "r")

line = inputs.readline()

orbit_map = {}

while line:
	central, orbiting = line.strip().split(")")

	if central not in orbit_map:
		orbit_map[central] = []

	if orbiting not in orbit_map:
		orbit_map[orbiting] = []

	orbit_map[central].append(orbiting)

	line = inputs.readline()



stack = ['COM']
distance_to_com = {}
distance_to_com['COM'] = 0

while len(stack):
	current = stack.pop()

	for planet in orbit_map[current]:
		stack.append(planet)
		distance_to_com[planet] = distance_to_com[current] + 1

print(sum([i for i in distance_to_com.values()]))