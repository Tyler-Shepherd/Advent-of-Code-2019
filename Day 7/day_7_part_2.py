import copy
import itertools

phases = set([i for i in range(5, 10)])

program_inputs = {}
programs = {}
program_loc = {}

last_output = None

amp_map = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'A'}

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

def compute_program(amplifier):
	global program_inputs, programs, program_loc, last_output

	current = program_loc[amplifier]
	program = programs[amplifier]

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
			program[args[0][0]] = program_inputs[amplifier].pop()
		elif operation == 4:
			output = get_param(args[0][1], program, args[0][0])
			last_output = output
			print "output", output

			programs[amplifier] = program
			program_loc[amplifier] = current + 2

			return output
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

	print "done", last_output
	return "DONE"



def run_amplifier(amp):
	global program_inputs, programs, program_loc, last_output, amp_map

	print "run amp", amp

	output = compute_program(amp)

	if output == "DONE":
		return last_output

	next_amp = amp_map[amp]

	program_inputs[next_amp].insert(0, output)

	return run_amplifier(next_amp)





inputs = open("./data.txt", "r")

program = [int(i) for i in inputs.readline().split(",")]

phase_combinations = itertools.permutations(phases)

max_result = None

amps = ['A', 'B', 'C', 'D', 'E']


for comb in phase_combinations:
	# assign inputs
	for i in range(len(comb)):
		amp = amps[i]

		program_inputs[amp] = [comb[i]]
		programs[amp] = copy.copy(program)
		program_loc[amp] = 0

	program_inputs['A'].insert(0,0)
	result = run_amplifier('A')

	print "result", result
	max_result = max(result, max_result)

	# reset
	program_inputs = {}
	programs = {}
	program_loc = {}


print "max", max_result