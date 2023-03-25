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
    isValid = verifyLink(arguments.weblink)
    if (not isValid):
        print("Please enter a valid URL")
        exit(0)
    
    chooseFunction(arguments.option, arguments.weblink)
    # if len(sys.argv) < 2:
    #     print("Enter a target website URL as an argument")
    #     sys.exit()
    #     exit(0)
    # elif len(sys.argv) > 2:
    #     print("Too many arguments, enter only 1 for the target website URL")
    #     sys.exit()
    #     exit(0)
    # else:
    #     """#Store argument if valid"""
    #     print("Argument Passed!")
    #     url = sys.argv[1]
    # cleanUrlPattern = r"(https?://)(?:www.)?([\w.-]+)"
    # cleanUrl = re.match(cleanUrlPattern, url)
    # findDirs(cleanUrl)
    # findSubDomains(cleanUrl)
    # getFiles(cleanUrl)

#     print(""" ██████████                █████                                                                                     
# ░░███░░░░░█               ░░███                                                                                      
#  ░███  █ ░  ████████    ███████   ██████   ██████   █████ █████  ██████  █████ ████ ████████     ████████  █████ ████
#  ░██████   ░░███░░███  ███░░███  ███░░███ ░░░░░███ ░░███ ░░███  ███░░███░░███ ░███ ░░███░░███   ░░███░░███░░███ ░███ 
#  ░███░░█    ░███ ░███ ░███ ░███ ░███████   ███████  ░███  ░███ ░███ ░███ ░███ ░███  ░███ ░░░     ░███ ░███ ░███ ░███ 
#  ░███ ░   █ ░███ ░███ ░███ ░███ ░███░░░   ███░░███  ░░███ ███  ░███ ░███ ░███ ░███  ░███         ░███ ░███ ░███ ░███ 
#  ██████████ ████ █████░░████████░░██████ ░░████████  ░░█████   ░░██████  ░░████████ █████     ██ ░███████  ░░███████ 
# ░░░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░  ░░░░░░   ░░░░░░░░    ░░░░░     ░░░░░░    ░░░░░░░░ ░░░░░     ░░  ░███░░░    ░░░░░███ 
#                                                                                                  ░███       ███ ░███ 
#                                                                                                  █████     ░░██████  
#                                                                                                 ░░░░░       ░░░░░░   """)

main()    
