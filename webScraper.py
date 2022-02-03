from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.newegg.ca/p/pl?d=graphic+cards'  # url that this program scrapes
client = uReq(url)
html_doc = client.read()  # Scrape the info
client.close()

htmlParsed = soup(html_doc, "html.parser")  # Parse the html document
graphicCards = htmlParsed.findAll("div", {"class": "item-container"}) # get info for each listing

fileName = "GraphicsCard.csv"
f = open(fileName, "w")

headers = "Brand Name, Product Name\n"  # Column names for my csv file

f.write(headers)

for eachGraphicCard in graphicCards:  # Iterate through each listing

    divFindBrand = eachGraphicCard.find("div", "item-branding")
    itemBrand = divFindBrand.find("a", "item-brand")
    getBrandName = ""
    if itemBrand is not None:
        imgBrand = itemBrand.find("img")
        getBrandName = imgBrand
    try:
        brandName = getBrandName.get('title')
    except AttributeError:
        pass

    title = eachGraphicCard.find("a", {"class": "item-title"})
    eachTitle = title.findAll(text=True, recursive=False)
    stringTitle = str(eachTitle)
    removeOpenBracket = stringTitle.replace("[", "")
    removeCloseBracket = removeOpenBracket.replace("]", "")
    finalTitle = removeCloseBracket.replace("'", "")

    print("Brand: " + str(brandName))
    print("Product Name: " + finalTitle)

    f.write(brandName + ", " + finalTitle.replace(",", "~") + "\n")
f.close()
