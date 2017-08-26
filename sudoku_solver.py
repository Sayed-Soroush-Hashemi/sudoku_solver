import sys
import time


def get_block_ind(r, c):
	block_width = int(len(table)**0.5)
	return int(r / block_width) * block_width + int(c / block_width)


def is_in_column(c, k):
	return columns[c][k]


def is_in_row(r, k):
	return rows[r][k]


def is_in_block(r, c, k):
	blockInd = get_block_ind(r, c)
	return blocks[blockInd][k]


def valid(r, c, k):
	return not (is_in_row(r, k) or is_in_column(c, k) or is_in_block(r, c, k))


# renamed "set" to "_set" to avoid ambiguity with python set data structure
def update(r, c, k, _set):
	table[r][c] = k if _set else 0
	columns[c][k] = _set
	rows[r][k] = _set
	blocks[get_block_ind(r, c)][k] = _set


def solve(r, c):
	if c >= len(table):
		return solve(r+1, 0)
	if r >= len(table):
		return True
	if table[r][c] != 0:
		return solve(r, c+1)
	for i in range(1, len(table)+1): 
		if valid(r, c, i):
			update(r, c, i, True)
			if solve(r, c+1):
				return True
			update(r, c, i, False)
	return False


def initialize():
	global table
	global rows
	global columns
	global blocks

	n = int(input())
	table = [[0] * n for i in range(n)]
	rows = [[False] * (n+1) for i in range(n)]
	columns = [[False] * (n+1) for i in range(n)]
	blocks = [[False] * (n+1) for i in range(n)]


def readInput():
	for r in range(len(table)):
		numbers = sys.stdin.readline().split()
		for c in range(len(table)):
			number = int(numbers[c])
			update(r, c, number, True)


def printAns():
	for r in range(len(table)):
		for c in range(len(table)):
			print(table[r][c]), 
		print('')
	


def main():
	global table
	global rows
	global columns
	global blocks
	table, rows, columns, blocks = [], [], [], []

	initialize()
	readInput()

	# print("solving ...")
	# start_time = time.time()
	if solve(0,0):
		printAns()
	else:
		print('unsolvable')
	# end_time = time.time()
	# elapsed_time = (end_time - start_time) / 1000.
	# print('running time {0}'.format(elapsed_time))


if __name__ == '__main__':
	main()