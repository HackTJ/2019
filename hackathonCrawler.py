#Web Crawler
from lxml import html
from lxml.etree import tostring

#Location Filter
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

from tqdm import tqdm
import json
import requests

page = requests.get("https://mlh.io/seasons/na-2018/events")
tree = html.fromstring(page.content)

link = tree.xpath('//a[@itemprop="url"]')
name = tree.xpath('//h3[@itemprop="name"]/text()')
imgs = tree.xpath('//div[@class="event-wrapper"]//div[@class="inner"]/div[@class="event-logo"]/img["src"]')
dates = tree.xpath('//div[@class="event-wrapper"]//div[@class="inner"]/p/text()')
city = tree.xpath('//span[@itemprop="addressLocality"]/text()')
state = tree.xpath('//span[@itemprop="addressRegion"]/text()')

link = [a.get('href') for a in link]
imgs = [a.get('src') for a in imgs]
dates = [a.strip() for a in dates if len(a.strip()) > 1]

hackathon_array = []
tj_loc = (38.818086, -77.168323)

for a in tqdm(range(len(name))):

    geolocator = Nominatim()
    location = geolocator.geocode(city[a]+", "+state[a])
    if(location):
        venue = (location.latitude, location.longitude)

        if(vincenty(tj_loc, venue).miles <= 240):

            hack = {
                "name": name[a],
                "img": imgs[a],
                "city": city[a],
                "state": state[a],
                "link": link[a],
                "date": dates[a],
            }
            
            hackathon_array.append(json.dumps(hack))

file = open("js/hackathonsList.js","w")
file.write("var hackathons = "+str(hackathon_array))

"""
var hackathons = {'UHack':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/725/thumb/u.png?1502746842','Miami','FL','http://uhackis.life/','Dec 2nd - 3rd'],'hackMCST':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/791/thumb/hackMCST_logo_100x100.png?1508361465','Denville','NJ','http://hackmcst.tech/','Dec 9th - 10th'],'Hack Arizona':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/793/thumb/arizona_logo.png?1509064266','Tucson','AZ','http://hackarizona.org/','Jan 12th - 14th'],'HackFRee':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/798/thumb/HACKFREE_100X100.png?1509490924','Manalapan','NJ','http://www.hackfree.info/','Jan 13th - 14th'],'nwHacks':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/799/thumb/nwhcks_logo.png?1509491135','Vancouver','BC','https://www.nwhacks.io/','Jan 13th - 14th'],'SwampHacks':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/795/thumb/swamphacks.png?1509110960','Gainesville','FL','http://2018.swamphacks.com/','Jan 19th - 21st'],'HackBI':['img/hackathon-logos/hackbi.png','Alexandria','VA','http://hackbi.org/','Jan 20th - 21th'],'Hoya Hacks':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/801/thumb/hoyahacks_appdog-01.png?1509542369','Washington','DC','http://www.hoyahacks.com/','Jan 26th - 28th'],'SheHacks':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/774/thumb/sheHacksboston_logo_100px_%281%29.jpg?1506548034','Boston','MA','http://shehacks.io/','Jan 26th - 28th'],'ConUHacks':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/751/thumb/CONUHACKS_LOGO_2017_MLH.png?1504810406','Montreal','QC','https://conuhacks.io/','Jan 27th - 28th'],'DeltaHacks IV':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/796/thumb/delta_logo.png?1509118107','Hamilton','ON','http://deltahacks.com/','Jan 27th - 28th'],'PixelHacks II':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/794/thumb/pixel_logo.png?1509110034','San Mateo','CA','http://pixelhacks.com/','Jan 27th - 28th'],'AthenaHacks':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/792/thumb/athena_logo.png?1509063263','Los Angeles','CA','http://athenahacks.com/','Feb 24th - 25th'],'HackFSU':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/691/thumb/mlh-logo.png?1500055957','Tallahassee','FL','https://www.hackfsu.com/','Mar 2nd - 4th'],'Hacklahoma':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/695/thumb/OK100x100.png?1500345654','Norman','OK','https://www.hacklahoma.org/','Mar 3rd - 4th'],'HackTJ':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/748/thumb/HackTJ_Logo_100.png?1504719770','Alexandria','VA','https://hacktj.org/','Mar 10th - 11th'],'LingHacks':['https://s3.amazonaws.com/assets.mlh.io/events/logos/000/000/700/thumb/LingScreenshot_2017-06-22_14.45.37.png?1500765718','Fremont','CA','http://linghacks.weebly.com/','Apr 7th - 8th']};
"""