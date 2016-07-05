import requests
from BeautifulSoup import BeautifulSoup

data = requests.get("https://icert.doleta.gov/").text

soup = BeautifulSoup(data)

# this is the id of the div we care about
fragment = soup.find(id="fragment-2")

# the data we care about is in the second 'em'. There are only two matching 
# elements and we care about the second one
date_as_of = fragment.findAll("em")[1].text

print "Date as of: %s" % date_as_of

processing_dates_table = fragment.findAll('table')[1].find('tbody')

for row in processing_dates_table.findAll('tr'):
    header = row.find('th').text
    
    try:
        month, year = [x.text.replace("&nbsp;","").strip() for x in \
                                                            row.findAll('td')]

        print "header: %s at %s/%s" % (header, month, year)
    except ValueError:
        pass
