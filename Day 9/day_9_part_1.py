import copy

user_inputs = [2]

relative_base = 0

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
	global relative_base

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
			program[loc] = user_inputs.pop()
		elif operation == 4:
			output = get_param(args[0][1], program, args[0][0])
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

result = compute_program(program)

# print "result", result