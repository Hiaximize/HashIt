#!/usr/bin/env python3
import hashlib
import sys

"""utilities"""
class bgColors:
    success = "\033[92m"
    endC = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    fail = '\033[91m'
    warning = '\033[93m'

helpMessage = f"""

    usage: ./hash.py [hash type: sha256|sha512] [option] [fileName/string] 

    {bgColors.underline}OPTIONS:{bgColors.endC}

        {bgColors.bold}-f{bgColors.endC} Hash a file

        {bgColors.bold}-s{bgColors.endC} Hash a string
"""

def printHash(finalHash):
    print("\n", finalHash, "\n")

def printError(error):
    if error.lower() == 'fail':
        print(f"\n{bgColors.fail}Error: Hash not created{bgColors.endC}\n")
    elif error.lower() == 'parameter':
        print(f"{bgColors.warning}Missing required arguments, please see below{bgColors.endC}")
        print(helpMessage)

if len(sys.argv) > 1:
    if sys.argv[1] == 'help' or sys.argv[1] == '-h':
        print(helpMessage)
    elif sys.argv[1] == "sha512" and sys.argv[2] == "-c" and sys.argv[3] == "-f":
        try:
            hashed = hashlib.sha512()
            with open(sys.argv[4], 'rb') as file:
                buffer = file.read()
                hashed.update(buffer)
            hashedFile = hashed.hexdigest()
            if hashedFile == sys.argv[5]:
                print(f'{bgColors.success}File Unaltered{bgColors.endC}')
            else:
                print(f"{bgColors.fail}Hashes don't match, I wouldn't run file{bgColors.endC}")
        except:
            printError('fail')
    elif sys.argv[1] == "sha256" and sys.argv[2] == "-f":
        try:
            hashed = hashlib.sha256()
            with open(sys.argv[3], 'rb') as file:
                buffer = file.read()
                hashed.update(buffer)
            printHash(hashed.hexdigest())
        except:
            # Improve this
            printError('fail')
    elif sys.argv[1] == "sha512" and sys.argv[2] == "-f":
        try:
            hashed = hashlib.sha512()
            with open(sys.argv[3], 'rb') as file:
                buffer = file.read()
                hashed.update(buffer)
            printHash(hashed.hexdigest())
        except:
            printError('fail')
    elif sys.argv[1] == "sha256" and sys.argv[2] == "-s":
        hashed = hashlib.sha256()
        hashed.update(bytes(sys.argv[3], 'utf-8'))
        print(hashed.hexdigest())
    elif sys.argv[1] == "sha512" and sys.argv[2] == "-s":
        hashed = hashlib.sha512()
        hashed.update(bytes(sys.argv[3], 'utf-8'))
        print(hashed.hexdigest())
else:
    printError('parameter')
    exit(1)