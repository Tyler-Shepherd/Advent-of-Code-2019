from fractions import gcd

inputs = open("./data.txt", "r")

asteroids = []

line = inputs.readline().strip()
y = 0
while line:
	for x in range(len(line)):
		if line[x] == '#':
			asteroids.append((x,y))

	line = inputs.readline().strip()
	y += 1


max_asteroid = None
max_seen = None

for a1 in asteroids:
	num_seen = 0

	for a2 in asteroids:
		if a1 == a2:
			continue

		x_diff = a1[0] - a2[0]
		y_diff = a1[1] - a2[1]

		factor = abs(gcd(x_diff, y_diff))

		x = a1[0]
		y = a1[1]

		hit_asteroid = False

		print "check", a1, a2, x_diff, y_diff, factor

		while True:
			x -= x_diff / factor
			y -= y_diff / factor

			print x, y

			if (x,y) == a2:
				break

			if (x,y) in asteroids:
				hit_asteroid = True
				break

		if not hit_asteroid:
			num_seen += 1

	if num_seen > max_seen:
		max_seen = num_seen
		max_asteroid = a1

print max_asteroid, max_seen