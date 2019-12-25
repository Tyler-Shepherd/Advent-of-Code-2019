import copy

inputs = open("./data.txt", "r")
# inputs = open("./example.txt", "r")

data = inputs.readline()

width = 25
height = 6
layers = len(data) / (width * height)

current_i = 0
current_j = 0
current_layer = 0

# construct array with correct size
image = [[] for x in range(layers)]
for layer in image:
	rows = [[] for x in range(height)]

	for row in rows:
		row.extend(None for x in range(width))

	layer.extend(rows)

# fill array
# i guess you don't actually need to store the full arrays for part 1
for digit in data:
	image[current_layer][current_j][current_i] = int(digit)

	current_i += 1
	if current_i == width:
		current_i = 0
		current_j += 1

		if current_j == height:
			current_j = 0
			current_layer += 1

# compute answer

def count_layer(num, layer):
	num_per_layer = 0

	for column in layer:
		num_per_layer += column.count(num)

	return num_per_layer



min_zeroes = float('inf')
layer_with_min = None

for layer in image:
	zeroes_on_layer = count_layer(0, layer)

	if zeroes_on_layer < min_zeroes:
		min_zeroes = zeroes_on_layer
		layer_with_min = copy.copy(layer)


num_ones = count_layer(1, layer_with_min)
num_twos = count_layer(2, layer_with_min)

print(num_ones * num_twos)