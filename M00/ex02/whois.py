import sys


def main():
    if len(sys.argv) == 1:
        return
    if len(sys.argv) > 2:
        print("Error: more than one argument")
        return
    elif not sys.argv[1].isnumeric():
        print("Error: not a number")
        return
    else:
        num = int(sys.argv[1])
        if num == 0:
            print("I'm Zero.")
        elif num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")


main()
