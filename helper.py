import re
import requests
import math
from tqdm import tqdm

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

def findDirs(cleanUrl: str, potential_dirs:list,progressbar):
    group1 = cleanUrl.group(1)
    group2 = cleanUrl.group(2)
    link = group1+group2
    num_valid = 0

    foundDirs = []

    for directory in potential_dirs:
        directory = directory.rstrip()
        fullURL = link+'/'+directory
        r = requests.get(fullURL)
        progressbar.update(1)
        if(r.status_code >= 200 and r.status_code <300):
            foundDirs.append(fullURL)
            num_valid+=1
    with open('output_files\dirs_output.txt','r') as out:
        for link in foundDirs:
            out.write(link+"\n")

def findSubDomains(cleanUrl: str):
    http = cleanUrl.group(1)
    link = cleanUrl.group(2)
    success = 0

    foundDoms = []

    for domain in domains:
        domain = domain.rstrip()
        try:
            r = requests.get(http+domain+"."+link)
            r.raise_for_status()
            if(r.status_code>=200 and r.status_code<300):
                Dom = http+domain+"."+link
                foundDoms.append(Dom)
                success+=1
        except requests.exceptions.RequestException as error:
            pass
    with open('output_files\subdomain_output.txt','r') as out:
        for link in foundDoms:
            out.write(link+"\n")
    
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
