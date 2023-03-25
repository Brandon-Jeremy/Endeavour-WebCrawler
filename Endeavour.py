import re
import sys
import threading
import requests
import tqdm
import argparse
from helper import *
from parser import *

arguments = parseArguments()

def main():
    print(arguments.weblink)
    validLink = verifyLink(arguments.weblink)
    if (not validLink):
        print("Please enter a valid URL")
        exit(0)
    print(validLink)
    try:
        chooseFunction(arguments.option, validLink)
    except KeyboardInterrupt:
        print("Keyboard Interrupt initiated")

    printAscii()

if __name__== "__main__":
    main()
