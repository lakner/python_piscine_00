import sys

arguments = sys.argv[1:]

if not arguments:
    sys.exit(0)

if len(arguments) > 1:
    print("AssertionError: more than one argument is provided")
else:
    try:
        arg = int(arguments[0])
        if arg % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError:
        print("AssertionError: argument is not an integer")
