import copy

inputs = open("./path.txt", "r")

path_1 = inputs.readline().split(",")
path_2 = inputs.readline().split(",")

def compute_points(path):
	points_along_path = set()

	current_loc = [0,0]
	for step in path:
		direction = step[0]
		distance = int(step[1:])

		for i in range(distance):
			if direction == 'D':
				current_loc[1] -= 1
			elif direction == 'U':
				current_loc[1] += 1
			elif direction == 'R':
				current_loc[0] += 1
			elif direction == 'L':
				current_loc[0] -= 1

			points_along_path.add(tuple(current_loc))

	return points_along_path

path_1_points = compute_points(path_1)
path_2_points = compute_points(path_2)

print(len(path_1_points))
print(len(path_2_points))

crossed_points = path_1_points.intersection(path_2_points)
print(crossed_points)

print(min(abs(i) + abs(j) for (i,j) in crossed_points))
