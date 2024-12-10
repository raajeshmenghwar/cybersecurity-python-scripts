#!/usr/bin/python3

# Importing necessary modules
import argparse  # For parsing command-line arguments
import sys       # To interact with the interpreter
import base64    # For base64 and base32 encoding/decoding

# Setting up argument parser with a description, usage instructions, and examples
parser = argparse.ArgumentParser(
    description="Python script to decode base64 or base32 encoding.",
    usage='%(prog)s --b64/--b32 cipher',
    epilog="Example - %(prog)s --base64 aGVsbG8="
)

# Adding an argument for base64 decoding
parser.add_argument(
    "--b64",           # The argument to look for in the command line
    help="decode base64 encoding",  # Description of the argument
    metavar="base64",  # A name for the expected value in help messages
    dest="b64",        # The attribute name to store the parsed value
    nargs="*"          # Accepts zero or more arguments (list of inputs)
)

# Adding an argument for base32 decoding
parser.add_argument(
    "--b32",           # The argument to look for in the command line
    help="decode base32 encoding",  # Description of the argument
    metavar="base32",  # A name for the expected value in help messages
    dest="b32",        # The attribute name to store the parsed value
    nargs="*"          # Accepts zero or more arguments (list of inputs)
)

# Adding an argument to display the script version
parser.add_argument(
    "-v",                  # Short option for version
    help="print version",  # Description of the argument
    action="version",      # Specifies this argument triggers the version display
    version="%(prog)s 1.0" # The version number to display
)

# Parsing the arguments
args = parser.parse_args()

# If no arguments are provided, print the help message and exit
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)  # Show the help message on standard error
    sys.exit(1)  # Exit with a status code indicating error

# Retrieving the parsed values for b64 and b32 arguments
b64 = args.b64
b32 = args.b32

# If base64 input is provided, decode each item and print the result
if b64:
    for i in b64:
        print((base64.b64decode(i)).decode())

# If base32 input is provided, decode each item and print the result
if b32:
    for i in b32:
        print((base64.b32decode(i)).decode())
