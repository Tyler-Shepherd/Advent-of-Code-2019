import copy

inputs = open("./path.txt", "r")

path_1 = inputs.readline().split(",")
path_2 = inputs.readline().split(",")

def compute_points(path):
	points_along_path = set()
	steps_to_point = {}

	current_loc = [0,0]
	steps_so_far = 0

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

			steps_so_far += 1
			tuple_loc = tuple(current_loc)
			points_along_path.add(tuple_loc)
			if tuple_loc not in steps_to_point:
				steps_to_point[tuple_loc] = steps_so_far

	return points_along_path, steps_to_point

path_1_points, path_1_steps_to_point = compute_points(path_1)
path_2_points, path_2_steps_to_point = compute_points(path_2)

print(len(path_1_points))
print(len(path_2_points))

crossed_points = path_1_points.intersection(path_2_points)
print(crossed_points)

print(min(path_1_steps_to_point[point] + path_2_steps_to_point[point] for point in crossed_points))
