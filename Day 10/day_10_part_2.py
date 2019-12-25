from fractions import gcd
from math import atan

inputs = open("./data.txt", "r")
# inputs = open("./example.txt", "r")

asteroids = []

line = inputs.readline().strip()
y = 0
while line:
	for x in range(len(line)):
		if line[x] == '#':
			asteroids.append((x,y))

	line = inputs.readline().strip()
	y += 1


laser_location = (26,29)
# laser_location = (8,3)



def get_destroyed_asteroids():
	global laser_location, asteroids

	top_right = {}
	bottom_right = {}
	bottom_left = {}
	top_left = {}

	for a in asteroids:
		if a == laser_location:
			continue

		x_diff = laser_location[0] - a[0]
		y_diff = laser_location[1] - a[1]

		factor = abs(gcd(x_diff, y_diff))

		x = laser_location[0]
		y = laser_location[1]

		hit_asteroid = False

		# print "check", a1, a2, x_diff, y_diff, factor

		while True:
			x -= x_diff / factor
			y -= y_diff / factor

			if (x,y) == a:
				break

			if (x,y) in asteroids:
				hit_asteroid = True
				break

		if not hit_asteroid:
			x_len = abs(a[0] - laser_location[0]) * 1.0
			y_len = abs(a[1] - laser_location[1]) * 1.0

			if y_len == 0:
				if a[0] > laser_location[0]:
					top_right[a] = float("inf")
				else:
					bottom_left[a] = float("inf")

			elif x_len == 0:
				if a[1] < laser_location[1]:
					top_right[a] = 0
				else:
					bottom_right[a] = 0

			else:
				angle = atan(x_len / y_len)

			if a[0] > laser_location[0] and a[1] < laser_location[1]:
				top_right[a] = angle
			elif a[0] > laser_location[0] and a[1] > laser_location[1]:
				bottom_right[a] = angle
			elif a[0] < laser_location[0] and a[1] > laser_location[1]:
				bottom_left[a] = angle
			elif a[0] < laser_location[0] and a[1] < laser_location[1]:
				top_left[a] = angle

	return top_right, bottom_right, bottom_left, top_left

# print get_destroyed_asteroids()

num_destroyed = 0

while len(asteroids) != 1:
	assert len(asteroids) > 0

	top_right, bottom_right, bottom_left, top_left = get_destroyed_asteroids()

	# print top_right
	# print bottom_right
	# print bottom_left
	# print top_left

	tr_ordered = sorted(top_right.items(), key = lambda kv:(kv[1], kv[0]))
	br_ordered = sorted(bottom_right.items(), key = lambda kv:(kv[1], kv[0]))
	br_ordered.reverse()
	bl_ordered = sorted(bottom_left.items(), key = lambda kv:(kv[1], kv[0]))
	tl_ordered = sorted(top_left.items(), key = lambda kv:(kv[1], kv[0]))
	tl_ordered.reverse()

	ordered_destruction = []
	ordered_destruction.extend(tr_ordered)
	ordered_destruction.extend(br_ordered)
	ordered_destruction.extend(bl_ordered)
	ordered_destruction.extend(tl_ordered)

	# print(ordered_destruction)

	for a in ordered_destruction:
		asteroids.remove(a[0])
		num_destroyed += 1

		print num_destroyed, a[0]

		if num_destroyed == 200:
			print "200th:", a[0]
			print a[0][0] * 100 + a[0][1]
			break

