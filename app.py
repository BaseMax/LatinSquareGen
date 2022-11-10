from LatinSquareGen import count_latin
from LatinSquareGen import list_latin

# order = 1
# order = 2
# order = 3 # 12
# order = 4 # 576
# order = 5 # 161280
# order = 6
# order = 7

# print(count_latin(order))
# print(list_latin(order))

# time_start = time.time_ns()

# print(count_latin(1)) # 0
# print(count_latin(2)) # 0
# print(count_latin(3)) # 0
# print(count_latin(4)) # 0
# print(count_latin(5)) # 1859719600ns = 1.8597196s
# print(count_latin(6)) # 1859719600


# 1
# 1666459033480935400
# 1666459033480935400
# 0
# 2
# 1666459033480935400
# 1666459033480935400
# 0
# 3
# 1666459033480935400
# 1666459033480935400
# 0
# 4
# 1666459033496556900
# 1666459033496556900
# 0
# 5
# 1666459033496556900
# 1666459035874167600
# 2377610700
# 6

# MAX = 7
# for i in range(1, MAX):
# 	print(i)

# 	time_start = time.time_ns()
# 	items = list_latin(i)
# 	time_end = time.time_ns()

# 	print(time_start)
# 	print(time_end)
# 	print(time_end - time_start)
	
# 	# create to file
# 	with open("latin_square_"+str(i)+".txt", "w") as f:
# 		for item in items:
# 			f.write(str(item))

# exit(1)

# time_start = time.time_ns()
# print(count_latin(5)) # 
# # list_latin(5)
# time_end = time.time_ns()
# print(time_start)
# print(time_end)
# print(time_end - time_start)

# # 161280
# # 1666411835152415700
# # 1666411837042330000
# # 1889914300 ns = 1.8899143 s

# time_start = time.time_ns()
# print(count_latin(6)) # 
# time_end = time.time_ns()
# print(time_start)
# print(time_end)
# print(time_end - time_start)

# # 812851200
# # 1666411837042330000
# # 1666424406427657700
# # 12569385327700 ns = 12569.385327700002 s


# time_start = time.time_ns()
# print(count_latin(7)) # 
# time_end = time.time_ns()
# print(time_start)
# print(time_end)
# print(time_end - time_start)

# def test(n):
# 	items = list_latin(n)
# 	# for item in items:
# 	# 	print(item)
# 	print(len(list(items)))

# test(1)
# test(2)
# test(3)
# test(4)
# test(5)

# handle arguments
# print arguments
