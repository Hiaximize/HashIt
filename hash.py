#!/usr/bin/env python3
import hashlib
import time
import os
import sys

"""utility class"""
class bgColors:
    success = "\033[92m"
    endC = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    fail = '\033[91m'
    warning = '\03393m'

helpMessage = f"""

    usage: ./hash.py [hash type] [option] [fileName/string] 

    {bgColors.underline}OPTIONS:{bgColors.endC}

        {bgColors.bold}-f{bgColors.endC} Hash a file

        {bgColors.bold}-s{bgColors.endC} Hash a string
"""

if len(sys.argv) > 1:
    if sys.argv[1] == "sha256" and sys.argv[2] == "-f":
        try:
            hashed = hashlib.sha256()
            with open(sys.argv[3], 'rb') as file:
                buffer = file.read()
                hashed.update(buffer)
            print('\n',hashed.hexdigest(),'\n')
        except:
            # Improve this
            print("Could not hash file")
    elif sys.argv[1] == "sha512" and sys.argv[2] == "-f":
        try:
            hashed = hashlib.sha512()
            with open(sys.argv[3], 'rb') as file:
                buffer = file.read()
                hashed.update(buffer)
            print("\n",hashed.hexdigest(),"\n")
        except:
            # Improve this
            print("Could not hash file")
    elif sys.argv[1] == "sha256" and sys.argv[2] == "-s":
        hashed = hashlib.sha256()
        hashed.update(bytes(sys.argv[3], 'utf-8'))
        print(hashed.hexdigest())
else:
    print("Missing required arguments, please see below")
    print(helpMessage)
    exit(1)
# myHash = hashlib.new('sha512')

# theInput = input("What do you want to hash> ")
# byteInput = bytes(theInput, 'ascii')
# print("Byte output", byteInput)
# myHash.update(byteInput)

# print(myHash.digest())

# print("Digest Size:", myHash.digest_size)

# hashed = hashlib.sha256(byteInput).hexdigest()
# print(hashed)