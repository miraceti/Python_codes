import xml.etree.ElementTree as ET

my_url='http://radiofrance-podcast.net/podcast09/rss_10212.xml'
#copy en local du xml home/eric/

root = ET.parse('rss_10212.xml').getroot()

filename = "latac28032020.csv"
f = open(filename, "w")

#tag channnel puis tag item puis tag enclosure
for type_tag in root.findall('channel/item/enclosure'):
#et puis tag url    
    value = type_tag.get('url')
    print(value)
    f.write(value + "\n")
