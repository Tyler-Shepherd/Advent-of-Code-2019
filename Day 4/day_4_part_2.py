range_min = 206938
range_max = 679128


def is_password_valid(num):
	num_as_str = str(num)

	current_count_same = 1
	adjacent_same = False

	for i in range(len(num_as_str) - 1):
		if num_as_str[i] == num_as_str[i+1]:
			current_count_same += 1
		else:
			if current_count_same == 2:
				adjacent_same = True
			current_count_same = 1


		if int(num_as_str[i]) > int(num_as_str[i+1]):
			return False

	if current_count_same == 2:
		return True

	return adjacent_same




# print(is_password_valid(112233)) # true
# print(is_password_valid(123444)) # false
# print(is_password_valid(111122)) # true


num_valid = 0

for i in range(range_min, range_max):
	if is_password_valid(i):
		num_valid += 1

print(num_valid)
