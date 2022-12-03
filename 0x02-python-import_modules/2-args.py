#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    arg_num = len(argv)

    if arg_num == 0:
        print("{} arguments.".format(arg_num))
    elif arg_num == 1:
        print("{} argument:".format(arg_num))
    elif arg_num  > 1:
        print("{} arguments:".format(arg_num))
    for i in range(arg_num):
        print("{}: {}".format(i+1, argv[i]))
