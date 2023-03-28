# Endeavour
Multithreaded python tool capable of finding all domains and subdirectories of a base URL. Also scrapes all links, either regular, video, image, or other from the source code. 
## Features
- Sends requests to subdomains and directories of the target website to check for valid pages
- Scrapes all links found in href tags on the target website
- Generates a report of all discovered pages and links
- Multi-threaded
- Others being added

## Requirements
- Python 3.x
- Requirements found in a requirements.txt document

## Installation
1. Clone the repository: `https://github.com/Brandon-Jeremy/Endeavour-WebScraper.git`
2. Install the required Python packages: `pip install -r requirements.txt`

## Usage
1. Navigate to the directory where the script is located: `cd <repository-name>`
2. Run the python script with: `python Endeavour.py <url>`
   -  Replace `<url>` with a target website (eg: `https://example.com`)

Current version of the code accepts arguments to denote the number of threads and which option to run on the target URL.

`python ./Endeavour.py https://example.com -o 1 -t 24` 

will allow you to run a general directory search on `https://example.com` with 24 threads.

## Testing
Additional test cases to be added soon.
1. Directories search run with arguments 
`python ./Endeavour <LINK> -o 1 -t 24` 
on an Intel i9-12th generation CPU with 24 threads took <1 minute to complete it's search.

## Comments
Additional features to be added soon. Main priority at the moment is improving on code efficiency and multithreading capabilites.