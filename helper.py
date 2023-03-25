import re
import requests

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
        return (isValid.status_code>=200 and isValid.status_code<300)
    except requests.exceptions.RequestException as error:
        return False
    
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
