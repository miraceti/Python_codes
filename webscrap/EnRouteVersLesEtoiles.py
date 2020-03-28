import xml.etree.ElementTree as ET
root = ET.parse('rss3.xml').getroot()
#Or any of the many other ways shown at ElementTree. Then do something like:
filename = "EnRouteVersLesEtoiles.csv"
f = open(filename, "w")


for type_tag in root.findall('channel/item/enclosure'):
    value = type_tag.get('url')
    print(value)
    f.write(value + "\n")


