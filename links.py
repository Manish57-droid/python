import requests
import re
import argparse
 
parser = argparse.ArgumentParser(
    description="Get list of links from a website"
)
 
parser.add_argument("url", nargs="?", help="URL", default=None)
 
arguments = parser.parse_args()
 
use_arguments = True if arguments.url is not None else False
 
# Check whether url will be obtained from command line argument
# or from user input
if use_arguments:
    url = arguments.url
else:
    while True:
        url = input("Enter the URL: ")
 
        if url == "":
            print("Invalid URL")
            continue
        break
 
html = requests.get(url).text
 
links = re.findall('"(https?://.*?)"', html)
 
for link in links:
    print(link)
