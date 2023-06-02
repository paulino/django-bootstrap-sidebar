#!/usr/bin/env python3
"""
GoogleFonts Downloader for Self-Hosted Webs

This script downloads selected fonts and changes the urls in the received CSS to
refer to local files. It generates a file named "fonts.css" that refers to the
"fonts" directory where the files are downloaded.

Example:

./gfontsdw.py 'https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,700;1,300;1,700&display=swap'

The recommended format is woff2, but the script downloads woff or ttf by
changing script settings.

The download URL is get selecting fonts in https://fonts.google.com and copying
the URL of the "link" or "import" statement::

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,700;1,300;1,700&display=swap');
    </style>

"""
import requests
import re
import sys
import os

__version__ = "1"

## Settings: the following options are not implemented as command line args

FORMAT = "woff2"  # Valid values "woff" or "ttf"

## End settings

if len(sys.argv) < 2:
    print(f"Google fonts downloader version {__version__}.\n")
    print(f"Usage: {sys.argv[0]} css_url")
    print(__doc__)
    sys.exit(255)

reg_url = r"src:.*url\(([^\)]*)"
g_url = sys.argv[1]

headers = {
    "woff2" : {
        'User-Agent' :'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'},
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

    "woff" : {
        'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    },
    "ttf" : {}

}

# Fonts output dir
if not os.path.exists("fonts"):
    os.mkdir("fonts")

css = requests.request("GET",g_url,headers=headers[FORMAT])
urls = re.findall(reg_url, css.text)

new_css = css.text
for url in urls:
    font_name = url.split("/")[-1]
    print(f"Download: fonts/{font_name}")
    res = requests.get(url, stream=True)
    with open(f"fonts/{font_name}", 'wb') as out_file:
        out_file.write(res.content)
    new_css = new_css.replace(url,f"fonts/{font_name}")

with open(f"fonts.css", 'w') as out_file:
    out_file.write(new_css)

print("Written: 'fonts.css'")

