user_inputs = [5]


def get_param(parameter_mode, program, param):
	if parameter_mode == 0:
		# position mode
		# print("get param", parameter_mode, param, program[param])
		return program[param]
	elif parameter_mode == 1:
		# print("get param", parameter_mode, param, program[param])
		return param
	else:
		print("BAD PARAMETER MODE", parameter_mode)

def compute_program(program):
	current = 0

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
		elif operation == 3 or operation == 4:
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
			program[args[2][0]] = get_param(args[0][1], program, args[0][0]) + get_param(args[1][1], program, args[1][0])
		elif operation == 2:
			program[args[2][0]] = get_param(args[0][1], program, args[0][0]) * get_param(args[1][1], program, args[1][0])
		elif operation == 3:
			program[args[0][0]] = user_inputs.pop()
		elif operation == 4:
			print(get_param(args[0][1], program, args[0][0]))
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
			third = args[2][0]

			if first < second:
				program[third] = 1
			else:
				program[third] = 0
		elif operation == 8:
			first = get_param(args[0][1], program, args[0][0])
			second = get_param(args[1][1], program, args[1][0])
			third = args[2][0]

			if first == second:
				program[third] = 1
			else:
				program[third] = 0
		else:
			print("BAD OP", opcode)

		# print("position", current, program)

		if not jumped:
			current += (len(args) + 1)

	return program

inputs = open("./part_1.txt", "r")

program = [int(i) for i in inputs.readline().split(",")]

result = compute_program(program)

print(result)