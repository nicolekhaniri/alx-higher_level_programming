#!/usr/bin/python3
import sys
argv = sys.argv[1:]
arg_num = len(argv)
if arg_num  == 0 or arg_num > 1:
     print(f"{arg_num} arguments")
elif arg_num  == 1:
     print(f"{arg_num} argument")
for i in range(arg_num):
    print(f"{i+1}: {argv[i]}")
