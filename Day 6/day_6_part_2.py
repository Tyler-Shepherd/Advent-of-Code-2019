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
	orbit_map[orbiting].append(central)

	line = inputs.readline()



stack = ['YOU']
visited = set()
distance_to_you = {}
distance_to_you['YOU'] = 0

while len(stack):
	current = stack.pop()
	visited.add(current)

	# print(current, orbit_map[current], distance_to_you)

	for planet in orbit_map[current]:
		if planet == 'SAN':
			print(distance_to_you[current] + 1 - 2)
			exit()

		if planet not in visited:
			stack.insert(0, planet)
			distance_to_you[planet] = distance_to_you[current] + 1
