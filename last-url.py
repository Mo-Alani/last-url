# A simple script to find the redirection history of a URL
# This can be useful in finding the ultimate URL after redirection to avoid pishing URLs
# Script created by Mohammed M. Alani (m@alani.me)
# The script is designed to run from the command line followed by the URL, or -h URL.
# The URL alone without -h would should you the last URL after redirection, and -h would show you the whol redirect history.
# Example:
# python last-url.py -h http://www.mohammedalani.com

import requests
import sys

commands = sys.argv

def get_the_url(url):
    try:
        history = []
        response = requests.get(url)
        for resp in response.history:
            history.append(resp.headers['Location'])
        history.insert(0,url)
    except:
        print("There's a problem in the URL!!! RUN!!!")
    return (history)

if len(commands) == 1:
    print('This script will show you the final URL for a redicrected URL.\nRun the script followed by the URL to get the final URL, or use "-h" to show all redirection URLs in the middle. Enjoy!!\nExample: python last-url.py -h http://www.mohammedalani.com')
    sys.exit()

if commands[1] == '-h':
    first_url = commands[2]
    h = get_the_url(first_url)
    for i in range(len(h)):
        msg = "URL " + str(i+1) +": "+ h[i]
        print(msg)
else:
    first_url = commands[1]
    h = get_the_url(first_url)
    print("Final URL: ", h[-1])

