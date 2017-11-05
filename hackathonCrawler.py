from lxml import html
from lxml.etree import tostring
import requests

page = requests.get("https://mlh.io/seasons/na-2018/events")
tree = html.fromstring(page.content)
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# prices = tree.xpath('//div[@class="item-price"]/text()')

link = tree.xpath('//a[@itemprop="url"]')
name = tree.xpath('//h3[@itemprop="name"]/text()')
imgs = tree.xpath('//div[@class="event-wrapper"]//div[@class="inner"]/div[@class="event-logo"]/img["src"]')
dates = tree.xpath('//div[@class="event-wrapper"]//div[@class="inner"]/p/text()')
city = tree.xpath('//span[@itemprop="addressLocality"]/text()')
state = tree.xpath('//span[@itemprop="addressRegion"]/text()')

link = [a.get('href') for a in link]
imgs = [a.get('src') for a in imgs]
dates = [a.strip() for a in dates if len(a.strip()) > 1]

# print(link)
# print(imgs)
# print(dates)

str = "var hackathons = {"
for a in range(len(name)):
    str += "'"+ name[a] + "':["
    str += "'"+ imgs[a] + "',"
    str += "'"+ city[a] + "',"
    str += "'"+ state[a] + "',"
    str += "'" + link[a] + "',"
    str += "'"+ dates[a] + "'],"
str = str[:-1] + "};"

file = open("js/hackathonsList.js","w")
file.write(str)