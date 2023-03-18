import requests

link = "https://ctflearn.com"

with open('subdomains_output.bat', 'w') as subdomains_output:
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


def fun():
    with open('subdomains_output.bat', 'w') as subdomains_output:
        with open('filesinuse/dirs_dictionary.bat','r') as potential_dirs:
            for linked in potential_dirs:
                linked = linked.rstrip()
                fullURL = link+'/'+linked
                print(fullURL)
                r = requests.get(fullURL)
                print(r.status_code)