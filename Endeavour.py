import re
import sys
import urllib.request
import time
import threading

"""#use: pip install requests to run code."""
import requests

def replace():
    with open('subdomains_output.bat', 'w') as subdomains_output:
        with open('filesinuse/subdomains_dictionary.bat','r') as potential_subs:
            for link in potential_subs:
                link = link.rstrip()
                parseLink = cleanUrl.group(1)+"www."+link+"."+cleanUrl.group(2)
                try:
                    r = requests.get(parseLink,timeout=3)

                    if (r.status_code):
                        print("Valid Subdomain: "+parseLink)
                        subdomains_output.write(parseLink+"\n")   
                except requests.HTTPError as error:
                    time.sleep(0)
                    #Do nothing
                    print(f"HTTP Exception occured: {error} of code: "+r.status_code)
                except Exception as error:
                    time.sleep(0)
                    #Do nothing
                    # print(f"Some other exception occured: {error}")

def replace2():
        pots = ['https://www.google.com','https://www.images.google.com']
        with open('subdomains_output.bat', 'w') as subdomains_output:
            for link in pots:
                try:
                    r = requests.get(link,timeout=3)
                    if(r.status_code):
                        print("Valid Subdomain: "+link)
                        subdomains_output.write(link)
                except requests.HTTPError as error:
                    print(f"HTTP Exception occured: {error} of code: "+r.status_code)
                except Exception as error:
                    print(f"Some other exception occured: {error}")

def findDirs(cleanUrl: str):
    group1 = cleanUrl.group(1)
    group2 = cleanUrl.group(2)
    link = group1+group2
    print("Main link: "+link)
    num_valid = 0
    with open('directories_output.bat', 'w') as directories_output:
        with open('filesinuse/dirs_dictionary.bat','r') as potential_dirs:
            for directory in potential_dirs:
                directory = directory.rstrip()
                print(directory)
                fullURL = link+'/'+directory
                print(fullURL)
                r = requests.get(fullURL)
                if(r.status_code >= 200 and r.status_code <300):
                    directories_output.write(fullURL+"\n")
                    num_valid+=1
                print(r.status_code)
    print(num_valid)

def findSubDomains(cleanUrl: str):
    testdomains = ['en','fr','sp']
    httptest = "https://"
    linktest = "wikipedia.org"
    http = cleanUrl.group(1)
    link = cleanUrl.group(2)
    success = 0
    with open('subdomains_output.bat','w') as subdomains_output:
        with open('filesinuse\subdomains_dictionary.bat','r') as domains:
            for domain in domains:
                domain = domain.rstrip()
                fullURL = http+"www."+domain+"."+link
                print(f"Link: {fullURL}")
                try:
                    r = requests.get(httptest+domain+"."+linktest)
                    r.raise_for_status()
                    if(r.status_code>=200 and r.status_code<300):
                        subdomains_output.write(httptest+domain+"."+linktest+"\n")
                        success+=1
                    print(r.status_code)
                except requests.exceptions.RequestException as error:
                    print(f"Connection error: {error}")
                except requests.exceptions.HTTPError as error:
                    #Do nothing
                    print(f"HTTP Exception occured: {error} of code: ",r.status_code)
                except Exception as error:
                    #Do nothing
                    print(f"Some other exception occured: {error}")
                except NewConnectionError as e:
                    print('Could not connect to server:', e)
    print(success)

def main():
    """#Check the arguments entered by the user"""
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
    url = "https://ctflearn.com"
    """#Clean the URL to try with subdomains"""
    cleanUrlPattern = r"(https?://)([\w.-]+)"
    cleanUrl = re.match(cleanUrlPattern, url)
    """#https://ctflearn.com"""
    # print(cleanUrl.group(2))
    """Expected Output: ctflearn.com"""
    # findDirs(cleanUrl)
    findSubDomains(cleanUrl)

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