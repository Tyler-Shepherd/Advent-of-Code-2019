import copy

def compute_program(program):
	current = 0

	while program[current] != 99:
		operation = program[current]
		first = program[current + 1]
		second = program[current + 2]
		output = program[current + 3]

		if operation == 1:
			program[output] = program[first] + program[second]
		elif operation == 2:
			program[output] = program[first] * program[second]

		current += 4

	return program


inputs = open("./intcode.txt", "r")

program_orig = [int(i) for i in inputs.readline().split(",")]


for noun in range(100):
	for verb in range(100):
		program = copy.copy(program_orig)

		program[1] = noun
		program[2] = verb

		result = compute_program(program)

		if result[0] == 19690720:
			print(noun, verb)