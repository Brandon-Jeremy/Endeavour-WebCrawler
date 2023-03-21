# Website Vulnerability Scanner
This is a tool that helps find vulnerabilities in a website by sending requests to different subdomains and directories to determine which ones are valid and which ones aren't. It also scrapes all links found in `href` tags on the target website.

## Features
- Sends requests to subdomains and directories of the target website to check for valid pages
- Scrapes all links found in href tags on the target website
- Generates a report of all discovered pages and links
- Multi-threaded (WIP)

## Requirements
- Python 3.x
- `requests` Python package

## Installation
1. Clone the repository: `https://github.com/Brandon-Jeremy/Endeavour-WebScraper.git`
2. Install the required Python package: `pip install requests`

## Usage
1. Navigate to the directory where the script is located: `cd <repository-name>`
2. Run the python script with: `python Endeavour.py <url>`
   -  Replace `<url>` with a target website (eg: `https://example.com`)
   -  For future updates specify a custom number of threads to run the script with for better efficiency as a command line argument.

## Example
```python
$python Endeavour.py https://example.com

#Expected output will vary depending on domain
#Output should resemble
https://example.com/dir1
200
https://example.com/dir2
404
https://subdomain.example.com
200
https://subdomain2.example.com
Connection error: {error_code}
```

Report will be saved into 3 separate files in the same directory as the script each containing information about scraped links, valid subdomains, and valid directories
