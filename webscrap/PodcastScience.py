from bs4 import BeautifulSoup as soup

fname = "PodcastScience.html"
htmlfile = open(fname,'r')
sourcecode = htmlfile.read()

page_soup = soup(sourcecode,"html.parser")
results2 = page_soup.findAll("a",attrs={'class':None})

filename = "podcastscience1.csv"
f = open(filename, "w")

for result2 in results2:
    print(result2.text)
    f.write(result2.text + "\n")
