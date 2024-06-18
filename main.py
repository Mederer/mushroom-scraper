from models.mushroom import Mushroom
from mushroom_parser import get_mushrooms

if __name__ == "__main__":
    print("Beginning to scrape mushrooms...")
    mushrooms = get_mushrooms(lambda x: print(x))

    print("Scraping complete. Scraped", len(mushrooms), "mushrooms.")
    print("Writing mushrooms to CSV...")

    Mushroom.write_to_csv(mushrooms)

    print("Finished!")