import sys


def main():
    # [1:] slices argv to remove first element. [start:stop]
    # [::-1] reverses the array. [start:stop:step]. -1 means last element.
    # using negative accessors [-1], [-2], etc. returns the last, second last, etc. element.
    args_rev = sys.argv[1:][::-1]
    for arg in args_rev:
        # [::-1] reverses string as discussed above.
        # .swapcase() swaps the case of the string.
        # we check if the current arg is the last arg in the array to decide whether to print space or not.
        print(arg[::-1].swapcase(), end=' ' if arg != args_rev[-1] else '')


main()
