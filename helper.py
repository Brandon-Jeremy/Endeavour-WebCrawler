import re
import requests
import math

from validations import *

def verifyLink(url:str):
    cleanUrlPattern = r"(https?://)(?:www.)?([\w.-]+)"
    validURL = re.match(cleanUrlPattern, url)
    """
    validURL.group(1) should always hold https://
    validURL.group(2) should always hold the link after www. regardless if www. is added
    """
    linkToUse = validURL.group(1)+validURL.group(2)
    try:
        isValid = requests.get(linkToUse)
        if (isValid.status_code>=200 and isValid.status_code<300):
            return validURL
        return None
    except requests.exceptions.RequestException as error:
        return None
    
def chooseFunction(argNumber: int, cleanUrl: str):
    if (argNumber == 1):
        findDirs(cleanUrl)
        
    elif(argNumber == 2):
        findSubDomains(cleanUrl)

    elif(argNumber == 3):
        getFiles(cleanUrl)

    else:
        findDirs(cleanUrl)
        findSubDomains(cleanUrl)
        getFiles(cleanUrl)

def findDirs(cleanUrl: str):
    group1 = cleanUrl.group(1)
    group2 = cleanUrl.group(2)
    link = group1+group2
    print("Main link: "+link)
    num_valid = 0
    with open('output_files/directories_output.txt', 'w') as directories_output:
        with open('input_files/dirs_dictionary.txt','r') as potential_dirs:
            for directory in potential_dirs:
                directory = directory.rstrip()
                fullURL = link+'/'+directory
                r = requests.get(fullURL)
                if(r.status_code >= 200 and r.status_code <300):
                    directories_output.write(fullURL+"\n")
                    num_valid+=1
    print(f"Number of valid directories: {num_valid}")

def findSubDomains(cleanUrl: str):
    http = cleanUrl.group(1)
    link = cleanUrl.group(2)
    success = 0
    with open('output_files/subdomains_output.txt','w') as subdomains_output:
        with open('input_files/subdomains_dictionary.txt','r') as domains:
            for domain in domains:
                domain = domain.rstrip()
                fullURL = http+"www."+domain+"."+link
                print(f"Link: {fullURL}")
                try:
                    r = requests.get(http+domain+"."+link)
                    r.raise_for_status()
                    if(r.status_code>=200 and r.status_code<300):
                        subdomains_output.write(http+domain+"."+link+"\n")
                        success+=1
                    print(r.status_code)
                except requests.exceptions.RequestException as error:
                    pass
    print(f"Number of valid subdomains: {success}")
    
def getFiles(cleanUrl: str):
    http=cleanUrl.group(0)
    link=cleanUrl.group(1)

    regex = r"<(?:a|link|img|video|audio) href=\"(.+?)\">"

    r = requests.get(http+link)
    source = r.text
    lst = re.findall(regex,source)
    with open('output_files/files_output.txt','w') as file_output:
        for link in lst:
            file_output.write(link+"\n")

def loadAndDivide(threadCount:int):
    with open('input_files\dirs_dictionary.txt','r') as dirs_file:
        dirs = dirs_file.read().splitlines()
        dirs = list(set(dirs))
    
    with open('input_files\subdomains_dictionary.txt','r') as subdomain_file:
        subdomains = subdomain_file.read().splitlines()
        subdomains = list(set(subdomains))

    sizeofDir = len(dirs)
    sizeofDom = len(subdomains)

    #Calculate the size that each thread should compute from the text file
    #Divide number of lines of file by the number of threads
    dir_jobsize = math.floor(sizeofDir/threadCount)
    subdom_jobsize = math.floor(sizeofDom/threadCount)

    divideDirs = []
    divideSubdoms = []
    for i in range(threadCount):
        if(i!=threadCount-1):
            #Compute starting and ending position for threds
            start = i*dir_jobsize
            end = start+dir_jobsize

            dirAdd = dirs[start:end]
            divideDirs.append(dirAdd)
        else:
            start = i*dir_jobsize

            dirAdd = dirs[start:]
            divideDirs.append(dirAdd)
    
    #Validation function
    # validateList(divideDirs)

    for i in range(threadCount):
        if(i!=threadCount-1):
            #Compute starting and ending position for threds
            start = i*subdom_jobsize
            end = start+subdom_jobsize
            
            subdomAdd = subdomains[start:end]
            divideSubdoms.append(subdomAdd)
        else:
            start = i*subdom_jobsize

            subdomAdd = subdomains[start:]
            divideSubdoms.append(subdomAdd)

    #Validation function
    # validateList(divideSubdoms)

    return ((dirs,divideDirs),(subdomains,divideSubdoms))

def printAscii():
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
