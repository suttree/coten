import re
import hashlib
#from dateutil.parser import parse
import os
from datetime import datetime, timedelta, timezone
import getpass
import sys


# Clippings parser from https://github.com/lvzon/kindle-clippings/blob/master/extract-kindle-clippings.py
infile = 'My Clippings.txt'

note_sep = '=========='

commentstr = '.. '  # RST (reStructuredText) comment

regex_title = re.compile('^(.*)\((.*)\)$')
regex_info = re.compile(r'^- (\S+) (.*)[\s|]+Added on\s+(.+)$')
regex_loc = re.compile('Loc\. ([\d\-]+)')
regex_page = re.compile('Page ([\d\-]+)')
regex_date = re.compile('Added on\s+(.+)$')

regex_hashline = re.compile('^\.\.\s*([a-fA-F0-9]+)' + '\s*')


pub_title = {}
pub_author = {}
pub_notes = {}
pub_hashes = {}

notes = {}
locations = {}
types = {}
dates = {}

note_hashes = []

existing_hashes = {}

print('Processing clippings file', infile)
        
mc = open(infile, 'r')

mc.read(1)  # Skip first character

line = mc.readline().strip()
        
while line:
    key = line.strip()
    result_title = regex_title.findall(key)    # Extract title and author
    line = mc.readline().strip()                # Read information line
    note_type, location, date = regex_info.findall(line)[0]    # Extract note type, location and date

    result_loc = regex_loc.findall(location)
    result_page = regex_page.findall(location)

    if len(result_title):
        title, author = result_title[0]
    else:
        title = key
        author = 'Unknown'
        
    if len(result_loc):
        note_loc = result_loc[0]
    else:
        note_loc = ''
        
    if len(result_page):
        note_page = result_page[0]
    else:
        note_page = ''
        
    note_text = ''
    line = mc.readline()                # Skip empty line
    line = mc.readline().strip()
        
    while line != note_sep:
        note_text += line + '\n'
        line = mc.readline().strip()
    
    note_hash = hashlib.sha256(note_text.strip().encode('utf8')).hexdigest()[:8]
    note_hashes.append(note_hash)

    if key not in pub_notes:
        pub_notes[key] = []
        pub_hashes[key] = []
        
    pub_title[key] = title.strip()
    pub_author[key] = author.strip()
    pub_notes[key].append(note_text.strip())
    pub_hashes[key].append(note_hash)
    
    locstr = ''
    if note_loc:
        locstr = 'loc.' + note_loc
    if note_page:
        if note_loc:
            locstr += ', '
        locstr += 'p.' + note_page
        
    try:
        datestr = str(parse(date))
    except:
        datestr = date
    
    notes[note_hash] = note_text.strip()
    locations[note_hash] = locstr
    types[note_hash] = note_type
    dates[note_hash] = datestr
        
    line = mc.readline().strip()
mc.close()

import pprint
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(notes)
#pp.pprint(pub_title)
#pp.pprint(pub_author)

import random
a = random.choice(note_hashes)
pp.pprint(note_hashes)
pp.pprint(notes[a])
pp.pprint(pub_title[a])
pp.pprint(pub_author[a])


# pick a random key
