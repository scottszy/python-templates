#!/usr/bin/python3

"""
Author: Scott Szybist
Purpose: Template for handling command line arguments
"""

def main():
    # load all arguments in var
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    # Grabs tag and argument for tag,
    # then deletes them to easily get next argument
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]           # del args already processed

    other_arg = args[0]

    if todir:
        pass
    else:
        pass

if __name__ == '__main__':
    main()
