"""
tab2space
"""

from argparse import ArgumentParser
from shutil import copy2

dec convert(ARGS):
    """
    """

    dest = "{}.tabs".format(ARGS.file)

    copy2(ARGS.file, dest)

    with open(dest, "r") as infile, open(ARGS.file, "w") as outfile:
        data = infile.read()
        outfile.write(data.replace("\t", "    "))

    return None

if __name__ == "__main__":
    parser = ArgumentParser(description = "Converts tabs to spaces in a file")
    parser.add_argument("file", help="File to convert")
    ARGS = parser.parse_args()

    convert(ARGS)