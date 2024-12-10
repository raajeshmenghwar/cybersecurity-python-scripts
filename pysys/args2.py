#!/usr/bin/python3

import argparse
import sys
import base64

parser = argparse.ArgumentParser(description="Python script to decode base64"
		,usage='%(prog)s --b64/--b32 cipher'
		,epilog="Example - %(prog)s --base64 aGVsbG8=")

parser.add_argument("--b64"
		,help="decode base64 encoding"
		,metavar="base64"
		,dest="b64"
		,nargs="*") #+ at least one argument, ? no need, * at least one or multiple arguments

parser.add_argument("--b32"
		,help="decode base32 encoding"
		,metavar="base32"
		,dest="b32"
		,nargs="*")

parser.add_argument("-v"
		,help="print version"
		,action="version"
		,version="%(prog)s 1.0")

args = parser.parse_args()

if len(sys.argv) == 1:
	parser.print_help(sys.stderr)
	sys.exit(1)


b64 = args.b64
b32 = args.b32

if b64:
	for i in b64:
		print((base64.b64decode(i)).decode())

if b32:
	for i in b32:
		print((base64.b32decode(i)).decode())
