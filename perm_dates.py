from BeautifulSoup import BeautifulSoup
from datetime import datetime
import os
import requests
import sqlite3

cur_dir = os.path.dirname(os.path.realpath(__file__))

conn = sqlite3.connect("%s/perm_dates.db" % cur_dir)
c = conn.cursor()

data = requests.get("https://icert.doleta.gov/").text

soup = BeautifulSoup(data)

# this is the id of the div we care about
fragment = soup.find(id="fragment-2")

# the data we care about is in the second 'em'. There are only two matching 
# elements and we care about the second one
date_as_of = fragment.findAll("em")[1].text

output = ""

output += "Date as of: %s\n" % date_as_of

processing_dates_table = fragment.findAll('table')[1].find('tbody')

for row in processing_dates_table.findAll('tr'):
    header = row.find('th').text
    
    try:
        month, year = [x.text.replace("&nbsp;","").strip() for x in \
                                                            row.findAll('td')]

        output += "header: %s at %s/%s\n" % (header, month, year)
    except ValueError:
        pass

last_data = c.execute("select timestamp, data from perm_dates order by timestamp desc limit 1;").fetchone()

c.execute("insert into perm_dates (timestamp, data) VALUES (?,?)", (datetime.now(), output))

conn.commit()

if last_data[-1] != output:
    print output
