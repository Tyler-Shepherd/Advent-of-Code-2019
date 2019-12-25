inputs = open("./data.txt", "r")
line = inputs.readline()

pos = []
vel = []

while line:
	parts = line.strip().split(",")

	x = int(parts[0][parts[0].find("=") + 1:])
	y = int(parts[1][parts[1].find("=") + 1:])
	z = int(parts[2][parts[2].find("=") + 1:parts[2].find(">")])

	pos.append([x,y,z])
	vel.append([0,0,0])

	line = inputs.readline()

num_planets = len(pos)

def update_velocity(i, j, x):
	if pos[i][x] < pos[j][x]:
		vel[i][x] += 1
	elif pos[i][x] > pos[j][x]:
		vel[i][x] -= 1

def update_position(i):
	pos[i][0] += vel[i][0]
	pos[i][1] += vel[i][1]
	pos[i][2] += vel[i][2]


for t in range(1000):
	for i in range(num_planets):
		for j in range(num_planets):
			if i == j:
				continue

			update_velocity(i,j,0)
			update_velocity(i,j,1)
			update_velocity(i,j,2)

	for i in range(num_planets):
		update_position(i)


# calculate energy

total_energy = sum(sum(abs(j) for j in pos[i]) * sum(abs(k) for k in vel[i]) for i in range(num_planets))

print total_energy