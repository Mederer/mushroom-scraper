from util import remove_html_tags
from models.mushroom import Mushroom
import requests
from bs4 import BeautifulSoup


def get_mushrooms(completion_callback=None):
    html_doc = requests.get("http://mushroom.world/mushrooms/namelist")
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    links = []
    mushrooms = []

    for link in soup.find_all('a'):
        if "/show" in link.get('href'):
            links.append("http://mushroom.world" + link.get('href'))

    for link in links:
        mushroom_doc = requests.get(link)
        mushroom_soup = BeautifulSoup(mushroom_doc.text, 'html.parser')

        name = None
        common_name = None
        family = None
        location = None
        dimensions = None
        edibility = None
        description = None

        try:
            common_name = mushroom_soup.find(
                "span", {"class": "mush-commonname"}).text[1:-1].rstrip()
        except:
            common_name = "None"

        try:
            name = mushroom_soup.find("b").text
            name = name[0:name.index("(")].strip()
        except:
            name = "None"

        divs = mushroom_soup.find("main").find_all(
            "div", {"class": "mush-info"})

        try:
            family = divs[0].find("div", {"class": "mush-textus"}).text
        except:
            family = "None"

        try:
            location = divs[1].find("div", {"class": "mush-textus"}).text
        except:
            location = "None"

        try:
            dimensions = divs[2].find("div", {"class": "mush-textus"}).text
        except:
            dimensions = "None"

        try:
            edibility = divs[3].find("div", {"class": "mush-textus"}).text
        except:
            edibility = "None"

        try:
            description_raw = divs[4].find(
                "div", {"class": "mush-longtextus"}).text
            description = remove_html_tags(description_raw)
        except:
            description = "None"

        try:
            images = []
            for img in mushroom_soup.find("div", {"class": "mush-images"}).find_all("img"):
                images.append("http://mushroom.world/" + img.get("src"))
        except:
            images = []

        mushroom = Mushroom(name, common_name, family.rstrip(), location.rstrip(
        ), dimensions.rstrip(), edibility.rstrip(), description.rstrip())
        mushroom.set_image_urls(images)
        mushrooms.append(mushroom)

        if completion_callback:
            completion_callback("Scraped " + name + "...")

    return mushrooms
