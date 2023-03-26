import argparse
import base64
import marshal
import os
import sys
import time
import zlib


def parse_args():
    parser = argparse.ArgumentParser(description="Simple Python Code Obfuscator")
    parser.add_argument("infile", help="Input file to obfuscate")
    parser.add_argument("outfile", help="Output file for obfuscated code")
    parser.add_argument(
        "-e", "--encoding", choices=["zlb", "b16", "b32", "b64", "mar"], default="mar", help="Select encoding method"
    )
    parser.add_argument("-n", "--note", default="# Obscated by Nuggy\n# https://nuggy.neverlose.wtf/s/7yatp01jtb\n", help="Add note to the obfuscated code")
    return parser.parse_args()


def get_input(prompt):
    if sys.version_info[0] == 2:
        return raw_input(prompt)
    elif sys.version_info[0] == 3:
        return input(prompt)
    else:
        sys.exit("\n Your Python Version is not Supported!")


def encode(encoding, data):
    if encoding == "zlb":
        return zlib.compress(bytes(data, 'utf-16'))
    elif encoding == "b16":
        return base64.b16encode(bytes(data, 'utf-16'))
    elif encoding == "b32":
        return base64.b32encode(bytes(data, 'utf-16'))
    elif encoding == "b64":
        return base64.b64encode(bytes(data, 'utf-16'))
    elif encoding == "mar":
        return marshal.dumps(compile(data, "<x>", "exec"))


def main():
    args = parse_args()
    with open(args.infile, "r") as infile:
        data = infile.read()

    encoded_data = encode(args.encoding, data)
    # write note
    with open(args.outfile, "w") as outfile:
        outfile.write(args.note)
    # append obfuscated data
    with open(args.outfile, "ab") as outfile:
        outfile.write(encoded_data)


if __name__ == "__main__":
    main()
