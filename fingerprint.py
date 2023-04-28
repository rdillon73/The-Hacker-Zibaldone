# fingerprint.py
import os

# we can also install missing tools by using the os library!
os.system(“pip install nmap”)

target = “website.com”
scan = “nmap -sS -p- -sV -sC -A -oA outputfile ”
os.system(scan + target)
