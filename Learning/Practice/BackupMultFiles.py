############################################################################################################
# A scirpts used to rename multi files at one time
# cmd exmaple: python .\BackupMultiFiles.py -b=backup ..\temp\input.txt ..\temp\output.txt
#
# Idea:
# 1. Use argparse and Template
# 2. Keep original file name
############################################################################################################
import argparse
import datetime
import os
from string import Template


def main():
    parser = argparse.ArgumentParser(description="Change file names")
    parser.add_argument(
        "files", metavar="file", type=str, nargs="*", help="the files to change"
    )
    parser.add_argument("-b", "--backup_label", type=str, default="bk")
    args = parser.parse_args()

    for file in args.files:
        timestamp = datetime.datetime.now().strftime("%Y%m%d")
        base, ext = os.path.splitext(file)
        print(base, timestamp, args.backup_label, ext)
        template = Template("$original_name-$timestamp-$backup$ext")
        new_name = template.safe_substitute(
            original_name=base, timestamp=timestamp, backup=args.backup_label, ext=ext
        )
        with open(file, "r") as f, open(new_name, "w") as new_f:
            new_f.write(f.read())


if __name__ == "__main__":
    main()
