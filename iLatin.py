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
order = 3 # 12
# order = 4 # 576
# order = 5 # 161280
# order = 6
# order = 7

print(count_latin(order))
print(list_latin(order))
