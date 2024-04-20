from bs4 import BeautifulSoup
from urllib.request import urlopen

from oceanic_cruise import OceanicCruise

if __name__ == "__main__":
    url = "https://campagnes.flotteoceanographique.fr/campagnes/18001350/fr/index.htm"
    # page = urlopen(url)
    # html = page.read().decode("utf-8")

    html = open("test_page.html", "r").read()

    soup = BeautifulSoup(html, "html.parser")
    oceanic_cruise = OceanicCruise(soup)
    oceanic_cruise.to_csv("test_output.csv", 'w')
