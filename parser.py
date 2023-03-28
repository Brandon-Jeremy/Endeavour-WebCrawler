import argparse

def parseArguments():
    parser = argparse.ArgumentParser(description='Python script to find all directories, subdomains,'+ 
    'and files in the source code.')

    parser.add_argument("weblink",help="Enter Link to crawl and find weaknesses",type=str)

    parser.add_argument("-o","--option",help="Select if you'd like to crawl directories (1), subdomains (2), "+
    "href links from source code (3) or all of the mentioned (4)",choices=[1,2,3,4],type=int, default=1)

    parser.add_argument("-t","--thread",help="Number of threads to execute code on",type=int, default=4)

    parser.add_argument("-v","--verbose",help="Choose if verbose mode should be enabled",choices=[True,False], type=bool, default=False)
    
    args = parser.parse_args()

    return args

