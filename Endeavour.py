import re
import sys
import threading
import requests
from tqdm import tqdm
import argparse
from helper import *
from parser import *
from threadManager import *

arguments = parseArguments()

def main():
    validLink = verifyLink(arguments.weblink)
    validThreadCount = verifyThreads(arguments.thread)
    if (not validLink):
        print("Please enter a valid URL")
        exit(0)
    try:
        # chooseFunction(arguments.option, validLink)
        loadAndDivide(validThreadCount)
    except KeyboardInterrupt:
        print("Keyboard Interrupt initiated")

    printAscii()

if __name__== "__main__":
    main()
