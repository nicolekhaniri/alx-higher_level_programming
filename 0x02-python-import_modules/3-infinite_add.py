#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    arg_num = len(argv)
    sum = 0
    if arg_num > 0:
        for i in range(arg_num):
            sum += int(argv[i])
            total = sum
        print("{}".format(total))
