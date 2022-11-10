#
# Name: Latin Square Gen
# Author: Max Base
# Date: 2022/10/20
# Repository: https://github.com/basemax/LatinSquareGen
#

import sys
import time

from LatinSquareGen import count_latin
from LatinSquareGen import list_latin

def help():
    print("LatinSquareGen - v1.0.0")
    print("")
    print("Commands:")
    print("-h, --help\t Show help")
    print("-v, --version\t Show version")
    print("-c, --create-latin\t Create an ordinary latin square")
    print("-rl, --create-random-latin\t Create a random latin square")
    print("-cl, --count-latin\t Count all latin squares in an order")
    print("")

# handle -h and --help
# handle -v and --version
# handle -c and --create-latin <n>
# handle -rl and --create-random-latin <n>
# handle -cl and --count-latin <n>
if len(sys.argv) == 1:
    help()
    sys.exit(1)
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    help()
elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
    print("LatinSquareGen - v1.0.0")
elif sys.argv[1] == "-c" or sys.argv[1] == "--create-latin":
    if len(sys.argv) == 3:
        order = int(sys.argv[2])
        items = list_latin(order)
        for item in items:
            print(item)
    else:
        print("Invalid arguments")
        help()
elif sys.argv[1] == "-rl" or sys.argv[1] == "--create-random-latin":
    if len(sys.argv) == 3:
        order = int(sys.argv[2])
        items = list_latin(order)
        for item in items:
            print(item)
    else:
        print("Invalid arguments")
        help()
elif sys.argv[1] == "-cl" or sys.argv[1] == "--count-latin":
    if len(sys.argv) == 3:
        order = int(sys.argv[2])
        print(count_latin(order))
    else:
        print("Invalid arguments")
        help()
else:
    print("Unknown command")
    help()
    sys.exit(1)
