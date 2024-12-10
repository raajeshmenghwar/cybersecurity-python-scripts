#!/usr/bin/python3

import sys
import base64

# Check if the user requested help or if the provided arguments are less than or equal to 2.
# If so, display usage instructions and exit the program.
if "-h" in sys.argv or len(sys.argv) <= 4:
    print(f"Usage - {sys.argv[0]} -b64/b32 -e/d cipher")
    sys.exit()

# Base64 Encoding Section
# Check if the user wants to encode with base64 ("-b64") and if the encode flag ("-e") is provided.
if "-b64" in sys.argv and "-e" in sys.argv:
    # Get the index of the "-e" flag to locate the cipher text in the arguments.
    index = (sys.argv).index("-e")
    # Encode the text using base64 encoding and print the result.
    b64encoded_string = base64.b64encode(sys.argv[index + 1].encode())
    print(b64encoded_string.decode())

# Base32 Encoding Section
# Check if the user wants to encode with base32 ("-b32") and if the encode flag ("-e") is provided.
if "-b32" in sys.argv and "-e" in sys.argv:
    # Get the index of the "-e" flag to locate the cipher text in the arguments.
    index = (sys.argv).index("-e")
    # Encode the text using base32 encoding and print the result.
    b32encoded_string = base64.b32encode(sys.argv[index + 1].encode())
    print(b32encoded_string.decode())

# Base64 Decoding Section
# Check if the user wants to decode with base64 ("-b64") and if the decode flag ("-d") is provided.
if "-b64" in sys.argv and "-d" in sys.argv:
    # Get the index of the "-d" flag to locate the cipher text in the arguments.
    index = (sys.argv).index("-d")
    # Decode the base64 encoded text and print the result.
    print((base64.b64decode(sys.argv[index + 1])).decode())

# Base32 Decoding Section
# Check if the user wants to decode with base32 ("-b32") and if the decode flag ("-d") is provided.
if "-b32" in sys.argv and "-d" in sys.argv:
    # Get the index of the "-d" flag to locate the cipher text in the arguments.
    index = (sys.argv).index("-d")
    # Decode the base32 encoded text and print the result.
    print((base64.b32decode(sys.argv[index + 1])).decode())

# If neither base64 nor base32 encoding/decoding was requested, display an error message.
if "-b64" not in sys.argv and "-b32" not in sys.argv:
    sys.stderr.write("Encoding Not Supported.")
