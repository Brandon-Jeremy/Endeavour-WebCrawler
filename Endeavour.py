import re
import sys
import threading
import requests
from tqdm import tqdm
import argparse
from concurrent.futures import ThreadPoolExecutor

from helper import *
from parser import *
from threadManager import *

arguments = parseArguments()

def runFunction(argNumber: int, cleanUrl: str, dirs, subdomains, validThreadCount:int):

    """
    ThreadPoolExecutor is best used with a with in order to have automatic 
    joins on the threads created. using with allows us to use it as a context manager
    to manage the creation and destruction of the pool.
    """

    progressbar = tqdm(range(len(dirs[0])),desc="Directories Search",colour="magenta",total=len(dirs[1][1]))
    findDirs(cleanUrl, dirs[1][0],progressbar)

def main():
    validLink = verifyLink(arguments.weblink)
    validThreadCount = verifyThreads(arguments.thread)
    if (not validLink):
        print("Please enter a valid URL")
        exit(0)
    try:
        dirs,subdomains = loadAndDivide(validThreadCount)     #loadAndDivide from helper.py

        all_dirs = dirs[0]
        divided_dirs = dirs[1]
        all_subdomains = subdomains[0]
        divided_subdomains = subdomains[1]

        if(arguments.option==5):
            #Later Addition for pws
            pass
        else:
            runFunction(arguments.option, validLink,dirs,subdomains, validThreadCount)
            pass
    except KeyboardInterrupt:
        print("Keyboard Interrupt initiated")

    # printAscii()

if __name__== "__main__":
    main()
