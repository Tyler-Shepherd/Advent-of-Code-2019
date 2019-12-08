range_min = 206938
range_max = 679128


def is_password_valid(num):
	num_as_str = str(num)

	adjacent_same = False

	for i in range(len(num_as_str) - 1):
		if num_as_str[i] == num_as_str[i+1]:
			adjacent_same = True

		if int(num_as_str[i]) > int(num_as_str[i+1]):
			return False

	return adjacent_same




# print(is_password_valid(122345)) # true
# print(is_password_valid(111123)) # true
# print(is_password_valid(111111)) # true
# print(is_password_valid(223450)) # false
# print(is_password_valid(123789)) # false


num_valid = 0

for i in range(range_min, range_max):
	if is_password_valid(i):
		num_valid += 1

print(num_valid)
