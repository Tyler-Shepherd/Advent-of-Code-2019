import copy
import pprint

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

final_image = [[] for x in range(height)]
for row in final_image:
	row.extend(None for x in range(width))


for j in range(height):
	for i in range(width):
		pixel_color = None

		for l in range(layers):
			if image[l][j][i] == 0 or image[l][j][i] == 1:
				pixel_color = image[l][j][i]
				break

		final_image[j][i] = pixel_color

pprint.pprint(final_image)
