import copy

current_x = 0
current_y = 0
grid = {(0,0): 1} # part 2
# grid = {(0,0): 0} # part 1

direction = "north"

relative_base = 0

should_paint = True


def move(turn_left):
	global direction, current_x, current_y, grid

	if direction == "north":
		if turn_left:
			current_x -= 1
			direction = "west"
		else:
			current_x += 1
			direction = "east"
	elif direction == "south":
		if turn_left:
			current_x += 1
			direction = "east"
		else:
			current_x -= 1
			direction = "west"
	elif direction == "west":
		if turn_left:
			current_y -= 1
			direction = "south"
		else:
			current_y += 1
			direction = "north"
	elif direction == "east":
		if turn_left:
			current_y += 1
			direction = "north"
		else:
			current_y -= 1
			direction = "south"



def get_param(parameter_mode, program, param):
	global relative_base

	if parameter_mode == 0:
		# position mode
		# print("get param", parameter_mode, param, program[param])
		if param in program:
			return program[param]
		return 0
	elif parameter_mode == 1:
		# exact mode
		# print("get param", parameter_mode, param, program[param])
		return param
	elif parameter_mode == 2:
		# relative mode
		if relative_base + param in program:
			return program[relative_base + param]
		return 0
	else:
		print("BAD PARAMETER MODE", parameter_mode)

def get_loc_param(parameter_mode, param):
	if parameter_mode == 0:
		return param
	elif parameter_mode == 2:
		return relative_base + param
	else:
		print "bad loc param", parameter_mode, parameter

def compute_program(program):
	global relative_base, direction, current_x, current_y, grid, should_paint

	current = 0

	output = None

	while program[current] != 99:
		opcode = str(program[current])
		operation = int(opcode[-1])
		parameter_modes = [int(i) for i in opcode[:-2]]

		args = []

		if operation == 1 or operation == 2 or operation == 7 or operation == 8:
			while len(parameter_modes) < 3:
				parameter_modes.insert(0, 0)

			args.append((program[current+1], parameter_modes.pop()))
			args.append((program[current+2], parameter_modes.pop()))
			args.append((program[current+3], parameter_modes.pop()))
		elif operation == 3 or operation == 4 or operation == 9:
			while len(parameter_modes) < 1:
				parameter_modes.insert(0, 0)

			args.append((program[current+1], parameter_modes.pop()))
		elif operation == 5 or operation == 6:
			while len(parameter_modes) < 2:
				parameter_modes.insert(0, 0)

			args.append((program[current+1], parameter_modes.pop()))
			args.append((program[current+2], parameter_modes.pop()))

		# print("opcode", opcode)
		# print("args", args)

		jumped = False

		if operation == 1:
			loc = get_loc_param(args[2][1], args[2][0])
			program[loc] = get_param(args[0][1], program, args[0][0]) + get_param(args[1][1], program, args[1][0])
		elif operation == 2:
			loc = get_loc_param(args[2][1], args[2][0])
			program[loc] = get_param(args[0][1], program, args[0][0]) * get_param(args[1][1], program, args[1][0])
		elif operation == 3:
			loc = get_loc_param(args[0][1], args[0][0])

			if (current_x, current_y) in grid:
				program[loc] = grid[(current_x, current_y)]
			else:
				program[loc] = 0
			
		elif operation == 4:
			output = get_param(args[0][1], program, args[0][0])
			assert output == 0 or output == 1

			if should_paint:
				grid[(current_x, current_y)] = output
				should_paint = False
			else:
				should_paint = True
				move(output)

			print "output", output
		elif operation == 5:
			first = get_param(args[0][1], program, args[0][0])
			second = get_param(args[1][1], program, args[1][0])
			if first != 0:
				current = second
				jumped = True
		elif operation == 6:
			first = get_param(args[0][1], program, args[0][0])
			second = get_param(args[1][1], program, args[1][0])
			if first == 0:
				current = second
				jumped = True
		elif operation == 7:
			first = get_param(args[0][1], program, args[0][0])
			second = get_param(args[1][1], program, args[1][0])
			third = get_loc_param(args[2][1], args[2][0])

			if first < second:
				program[third] = 1
			else:
				program[third] = 0
		elif operation == 8:
			first = get_param(args[0][1], program, args[0][0])
			second = get_param(args[1][1], program, args[1][0])
			third = get_loc_param(args[2][1], args[2][0])

			if first == second:
				program[third] = 1
			else:
				program[third] = 0
		elif operation == 9:
			relative_base += get_param(args[0][1], program, args[0][0])
		else:
			print("BAD OP", opcode)

		# print("position", current, program)

		if not jumped:
			current += (len(args) + 1)

	return output



inputs = open("./data.txt", "r")

program_list = [int(i) for i in inputs.readline().split(",")]
program = {}
for i in range(len(program_list)):
	program[i] = program_list[i]


compute_program(program)

print "painted", len(grid.keys())

min_x = min(i for (i,j) in grid.keys())
max_x = max(i for (i,j) in grid.keys())
min_y = min(j for (i,j) in grid.keys())
max_y = max(j for (i,j) in grid.keys())

for x in range(min_x, max_x + 1):
	current_paint = ""
	for y in range(min_y, max_y + 1):
		if (x,y) in grid:
			if grid[(x,y)]:
				current_paint += "**"
			else:
				current_paint += "  "
			# current_paint += str(grid[(x,y)])
		else:
			current_paint += "  "
	print(current_paint)