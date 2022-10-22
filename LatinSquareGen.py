#
# Name: Latin Square Gen
# Repository: https://github.com/basemax/LatinSquareGen
# Author: Max Base
# Date: 2022/10/20
#

import time

def row(n, r, c = []):
	row_list = []
	len_c = len(c)

	if len_c == n:
		row_list.append(c)

	for i in range(1, n + 1):
		if i not in c and i not in r[len_c]:
			arr = row(n, r, c + [i])
			for i in arr:
				row_list.append(i)

	return row_list

def count_row(n, k, r, c = []):
	row_list = 0
	len_c = len(c)

	if len_c == n:
		row_list += count_latin(n, k + [c])

	for i in range(1, n + 1):
		if i not in c and i not in r[len_c]:
			row_list += count_row(n, k, r, c + [i])

	return row_list

def count_latin(n, k = []):
	if len(k) == n:
		return 1
	else:
		if not k:
			r = [[]] * n
		else:
			r = list(zip(*k))
		return count_row(n, k, r)

def list_latin(n, c = []):
	latin_list = []

	if len(c) == n:
		latin_list.append(c)
	else:
		if not c:
			r = [[]] * n
		else:
			r = list(zip(*c))

		rows = row(n, r)
		for i in rows:
			arr = list_latin(n, c+[i])
			for i in arr:
				latin_list.append(i)

	return latin_list

# order = 1
# order = 2
# order = 3 # 12
# order = 4 # 576
# order = 5 # 161280
# order = 6
# order = 7

# print(count_latin(order))
# print(list_latin(order))

time_start = time.time_ns()

# print(count_latin(1)) # 0
# print(count_latin(2)) # 0
# print(count_latin(3)) # 0
# print(count_latin(4)) # 0
# print(count_latin(5)) # 1859719600ns = 1.8597196s
# print(count_latin(6)) # 1859719600

time_start = time.time_ns()
print(count_latin(5)) # 
# list_latin(5)
time_end = time.time_ns()
print(time_start)
print(time_end)
print(time_end - time_start)

# 161280
# 1666411835152415700
# 1666411837042330000
# 1889914300 ns = 1.8899143 s

time_start = time.time_ns()
print(count_latin(6)) # 
time_end = time.time_ns()
print(time_start)
print(time_end)
print(time_end - time_start)

# 812851200
# 1666411837042330000
# 1666424406427657700
# 12569385327700 ns = 12569.385327700002 s


time_start = time.time_ns()
print(count_latin(7)) # 
time_end = time.time_ns()
print(time_start)
print(time_end)
print(time_end - time_start)
