#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv[1:]
    arg_num = len(argv)
    if arg_num > 0:
        for i in range(arg_num):
            a = argv[1]
            b = argv[2]
            a = int(a)
            b = int(b)
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
