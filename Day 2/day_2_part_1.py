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

program = [int(i) for i in inputs.readline().split(",")]

program[1] = 12
program[2] = 2

result = compute_program(program)

print(result)