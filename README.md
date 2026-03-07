# Last URL
`last-url` is s simple python script written to resolve the last URL from a redirection URL. You know how annoying it could be receiving this _bit.ly_ link that you don't know where it leads? This is the script for you.

***

## Downloading the script
On your machine just type:

`git clone https://github.com/Mo-Alani/last-url.git`

***

## How to use the script
The script was written to be a simple command line script to resolve the final URL after redirection.
To get the final URL only (without the rest of the redirection history):

`python last-url.py -u http://your-URL-here`

or

`python3 last-url.py -u http://your-URL-here`

If you want to see the full history of redirections (all the intermediate links, if any):

`python last-url.py -u http://your-URL-here -f`

or

`python3 last-url.py -u http://your-URL-here -f`

If the URL has "&" in it, you'll need to wrap it with quotation marks:

`python last-url.py -u "http://your-URL-here-with-&-character" -f`

or

`python3 last-url.py -u "http://your-URL-here-with-&-character" -f`

## Example:

        git clone https://github.com/Mo-Alani/last-url.git
        cd last-url
        python last-url.py -u http://mohammedalani.com -h

## Contributors
Mohammed M. Alani ([@Mo-Alani](https://github.com/Mo-Alani))