# A simple script to find the redirection history of a URL
# This can be useful in finding the ultimate URL after redirection to avoid pishing URLs
# Script created by Mohammed M. Alani (m@alani.me)
# The script is designed to run from the command line followed by the URL, or -h URL.
# The URL alone without -h would should you the last URL after redirection, and -h would show you the whol redirect history.
# Example:
# python last-url.py -h http://www.mohammedalani.com

import requests
import sys
import argparse

def get_the_url(url):
    try:
        history = []
        response = requests.get(url)
        for resp in response.history:
            history.append(resp.headers['Location'])
        history.insert(0,url)
    except:
        print("The URL couldn't be resolved!!! RUN!!!")
    return (history)

parser = argparse.ArgumentParser(description="last-url is a small tool designed to find the last URL in a redirected URL.\npython last-url.py --url https://mohammedalani.com -h")
parser.add_argument("-u","--url", metavar="url", type=str, help="The URL you want to resolve")
parser.add_argument("-f","--full", action='store_true', help="Show the full history of redirections until the last URL.")

args = parser.parse_args()

print("Looking up this suspicious URL for you...")

if (not args.url):
    parser.print_help()
    sys.exit()

h = get_the_url(args.url)

if (not args.full):
        print(f"Last URL is: {h[-1]}")
else:
        for i in range(len(h)):
            print(f"URL {i+1}: {h[i]}")



    
