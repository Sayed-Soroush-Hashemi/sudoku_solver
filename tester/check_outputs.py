import glob
import os
import re
import pprint; pprint = pprint.PrettyPrinter(indent=4).pprint


def read_tables(input_file_path, output_file_path):
	with open(input_file_path, 'r') as input_file:
		input_table = [[int(num) for num in row.split()] for row in input_file]
		input_table = input_table[1:]

	with open(output_file_path, 'r') as output_file:
		output_table = [[int(num) for num in row.split()] for row in output_file]

	return input_table, output_table


def check_tables_size(input_table, output_table):
	error_message = "input and output tables' sizes doesn't match"
	if len(input_table) != len(output_table):
		print(error_message)
		return False
	for i in range(len(input_table)):
		if len(input_table[i]) != len(output_table[i]):
			print(error_message)
			return False
	return True


def check_substitution_mistakes(input_table, output_table):
	error_message = "a fixed cell in input table changed"
	for r in range(len(input_table)):
		for c in range(len(input_table[r])):
			if input_table[r][c] != 0 and input_table[r][c] != output_table[r][c]:
				print(error_message)
				return False
	return True


def check_numbers_range(output_table):
	error_message = 'cell numbers out of range'
	for r in range(len(output_table)):
		for c in range(len(output_table)):
			if not (0 < output_table[r][c] and output_table[r][c] <= len(output_table)):
				print(error_message)
				return False
	return True


def check_uniqueness_in_rows(output_table):
	error_message = "duplicate numbers in row {0}"
	for r in range(len(output_table)):
		temp = set(output_table[r])
		if len(temp) != len(output_table):
			print(error_message.format(r+1))
			return False
	return True


def check_uniqueness_in_columns(output_table):
	error_message = "duplicate numbers in column {0}"
	for c in range(len(output_table)):
		column_numbers = [output_table[r][c] for r in range(len(output_table))]
		temp = set(column_numbers)
		if len(temp) != len(output_table):
			print(error_message.format(c+1))
			return False
	return True


def get_block_ind(r, c, n):
	block_width = int(n ** 0.5)
	return int(r / block_width) * block_width + int(c / block_width)


def check_uniqueness_in_blocks(output_table):
	error_message = "duplicate numbers in block {0}"
	block_numbers = [[] for block_ind in range(len(output_table))]
	for r in range(len(output_table)):
		for c in range(len(output_table)):
			block_ind = get_block_ind(r, c, len(output_table))
			block_numbers[block_ind].append(output_table[r][c])
	for block_ind in range(len(block_numbers)):
		temp = set(block_numbers[block_ind])
		if len(temp) != len(block_numbers[block_ind]):
			print(error_message.format(block_ind+1))
			return False
	return True


def check_validity(output_table):
	return check_uniqueness_in_rows(output_table) and \
			check_uniqueness_in_columns(output_table) and \
			check_uniqueness_in_blocks(output_table)


def is_input_unsolvable(input_file_path):
	return 'unsolvable' in input_file_path


def is_output_unsolvable(output_file_path):
	with open(output_file_path, 'r') as output_file:
		answer = output_file.read().strip()
		return answer == 'unsolvable'


def check_single_test(input_file_path, output_file_path):
	if is_input_unsolvable(input_file_path):
		if is_output_unsolvable(output_file_path):
			return True
		return False

	input_table, output_table = read_tables(input_file_path, output_file_path)
	if check_tables_size(input_table, output_table) and \
			check_substitution_mistakes(input_table, output_table) and \
			check_numbers_range(output_table) and \
			check_validity(output_table):
		return True
	print('input table: ')
	pprint(input_table)
	print('output table: ')
	pprint(output_table)
	return False


def main():
	for file_name in glob.glob('inputs/*.txt'):
		file_name = re.findall('inputs/(.*)', file_name)[0]
		input_file_path = os.path.join('inputs', file_name)
		output_file_path = os.path.join('outputs', file_name)

		test_name = '.'.join(file_name.split('.')[:-1])
		print('running test {0} . . . '.format(test_name)),
		if not check_single_test(input_file_path, output_file_path):
			print('failed')
		else:
			print('OK')


if __name__ == '__main__':
	main()
