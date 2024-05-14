############################################################################################################
# A scirpts used to print multi files with top x lines.
# cmd exmaple: python .\ExtractFileWithTopLines.py --lines=6 ..\temp\input.txt ..\temp\output.txt
#
# Idea:
# 1. Use argparse for receiving params from cmd line, and os for checking whether it's file or not
# 2. Define 2 params: -l for lines, filenames as free param
# 3. Iterate the files and open them, print top x lines with splitlines function
############################################################################################################

import argparse
import os


def main():
    parse = argparse.ArgumentParser(
        prog="TopXLines",
        description="A script used to print top x lines for certain files",
    )

    parse.add_argument("filenames", nargs="*")
    parse.add_argument(
        "-l",
        "--lines",
        type=int,
        default=5,
        help="Input the numbers of lines you want to print",
    )
    args = parse.parse_args()

    for file in args.filenames:
        if os.path.isfile(file):
            with open(file) as f:
                print(f.read().splitlines()[: args.lines])
        else:
            print(file, "is not a valid file, pleae check")


if __name__ == "__main__":
    main()
