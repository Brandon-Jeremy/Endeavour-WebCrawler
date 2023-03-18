import requests
from urllib3.exceptions import NewConnectionError


link = "https://ctflearn.com"
http = "https://"
subdomain = ''
link = "wikipedia.org"
subdomains = ['en.','fr.','sp.']
#Valid Valid Invalid

with open('subdomains_output.bat','w') as subdomains_output:
    for subdomain in subdomains:
        try:
            r = requests.get(http+subdomain+link)
            r.raise_for_status()
            if(r.status_code>=200 and r.status_code<300):
                subdomains_output.write(http+subdomain+link+"\n")
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


def workingDir():
    with open('directories_output.bat', 'w') as directories_output:
        with open('filesinuse/dirs_dictionary.bat','r') as potential_dirs:
            for directory in potential_dirs:
                directory = directory.rstrip()
                print(directory)
                fullURL = link+'/'+directory
                print(fullURL)
                r = requests.get(fullURL)
                if(r.status_code >= 200 and r.status_code <300):
                    subdomains_output.write(fullURL)
                print(r.status_code)

def functional():
    with open('subdomains_output.bat', 'w') as subdomains_output:
        with open('filesinuse/dirs_dictionary.bat','r') as potential_dirs:
            for linked in potential_dirs:
                linked = linked.rstrip()
                fullURL = link+'/'+linked
                print(fullURL)
                r = requests.get(fullURL)
                print(r.status_code)