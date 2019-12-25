from copy import deepcopy
from fractions import gcd

inputs = open("./data.txt", "r")
line = inputs.readline()

pos = []
vel = []

def lcm(a):
	result = a[0]
	for i in a[1:]:
  		result = result*i/gcd(result, i)

  	return result

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

def update_position(i, x):
	pos[i][x] += vel[i][x]


original_pos = deepcopy(pos)
original_vel = deepcopy(vel)

steps_to_repeat = []

for p in range(3):
	t = 0
	while True:
		for i in range(num_planets):
			for j in range(num_planets):
				if i == j:
					continue

				update_velocity(i,j,p)

		for i in range(num_planets):
			update_position(i, p)

		t += 1

		if original_pos == pos and original_vel == vel:
			steps_to_repeat.append(t)
			print pos, vel, t
			break

print steps_to_repeat
print lcm(steps_to_repeat)