import re
import sys
import urllib.request
import time
import threading

"""#use: pip install requests to run code."""
import requests

def findSubdomains(cleanUrl: str):
    # print("group1: "+cleanUrl.group(1))
    # print("group2: "+cleanUrl.group(2))
    with open('subdomains_output.bat', 'w') as subdomains_output:
        with open('filesinuse/subdomains_dictionary.bat','r') as potential_subs:
            for link in potential_subs:
                link = link.rstrip()
                parseLink = cleanUrl.group(1)+"www."+link+"."+cleanUrl.group(2)
                r = requests.get(parseLink)
                if r.getcode()<200 or r.getcode()>=300:
                    print ("Website Error: ", url, r)
                else:
                    print ("Website Passed: ", url, r)
                # if (r.status_code >= 200 and r.status_code <=299):
                    # print("Valid Subdomain: "+parseLink)
                subdomains_output.write(parseLink+"\n")
            
def main():
    """#Check the arguments entered by the user"""
    if len(sys.argv) < 2:
        print("Enter a target website URL as an argument")
        sys.exit()
        exit(0)
    elif len(sys.argv) > 2:
        print("Too many arguments, enter only 1 for the target website URL")
        sys.exit()
        exit(0)
    else:
        """#Store argument if valid"""
        print("Argument Passed!")
        url = sys.argv[1]

    """#Clean the URL to try with subdomains"""
    cleanUrlPattern = r"(https?://)([\w.-]+)"
    cleanUrl = re.match(cleanUrlPattern, url)
    """#https://ctflearn.com"""
    # print(cleanUrl.group(2))
    """Expected Output: ctflearn.com"""
    findSubdomains(cleanUrl)

    time.sleep(1)

    print(""" ██████████                █████                                                                                     
░░███░░░░░█               ░░███                                                                                      
 ░███  █ ░  ████████    ███████   ██████   ██████   █████ █████  ██████  █████ ████ ████████     ████████  █████ ████
 ░██████   ░░███░░███  ███░░███  ███░░███ ░░░░░███ ░░███ ░░███  ███░░███░░███ ░███ ░░███░░███   ░░███░░███░░███ ░███ 
 ░███░░█    ░███ ░███ ░███ ░███ ░███████   ███████  ░███  ░███ ░███ ░███ ░███ ░███  ░███ ░░░     ░███ ░███ ░███ ░███ 
 ░███ ░   █ ░███ ░███ ░███ ░███ ░███░░░   ███░░███  ░░███ ███  ░███ ░███ ░███ ░███  ░███         ░███ ░███ ░███ ░███ 
 ██████████ ████ █████░░████████░░██████ ░░████████  ░░█████   ░░██████  ░░████████ █████     ██ ░███████  ░░███████ 
░░░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░  ░░░░░░   ░░░░░░░░    ░░░░░     ░░░░░░    ░░░░░░░░ ░░░░░     ░░  ░███░░░    ░░░░░███ 
                                                                                                 ░███       ███ ░███ 
                                                                                                 █████     ░░██████  
                                                                                                ░░░░░       ░░░░░░   """)

main()    